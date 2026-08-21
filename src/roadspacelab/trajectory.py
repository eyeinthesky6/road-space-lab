"""Dependency-free descriptors for 2-D vehicle trajectories."""
from __future__ import annotations

import math
from statistics import fmean, pstdev
from typing import Sequence


def _validate_xy(x_m: Sequence[float], y_m: Sequence[float]) -> None:
    if len(x_m) != len(y_m):
        raise ValueError("x_m and y_m must have equal length")
    if len(x_m) < 2:
        raise ValueError("at least two points are required")


def _quantile(values: Sequence[float], q: float) -> float:
    if not values:
        raise ValueError("values cannot be empty")
    if not 0 <= q <= 1:
        raise ValueError("q must be in [0, 1]")
    ordered = sorted(float(v) for v in values)
    if len(ordered) == 1:
        return ordered[0]
    pos = (len(ordered) - 1) * q
    lo, hi = math.floor(pos), math.ceil(pos)
    if lo == hi:
        return ordered[lo]
    w = pos - lo
    return ordered[lo] * (1 - w) + ordered[hi] * w


def lateral_excursion(y_m: Sequence[float], lower_q: float = 0.05, upper_q: float = 0.95) -> float:
    """Robust lateral envelope (default P95-P05), metres."""
    if lower_q >= upper_q:
        raise ValueError("lower_q must be < upper_q")
    return _quantile(y_m, upper_q) - _quantile(y_m, lower_q)


def path_length(x_m: Sequence[float], y_m: Sequence[float]) -> float:
    """Distance travelled along the observed two-dimensional path."""
    _validate_xy(x_m, y_m)
    return sum(math.hypot(x_m[i] - x_m[i - 1], y_m[i] - y_m[i - 1]) for i in range(1, len(x_m)))


def path_tortuosity(x_m: Sequence[float], y_m: Sequence[float]) -> float:
    """Observed path length / direct displacement. 1.0 is perfectly straight."""
    _validate_xy(x_m, y_m)
    direct = math.hypot(x_m[-1] - x_m[0], y_m[-1] - y_m[0])
    if direct == 0:
        return math.inf
    return path_length(x_m, y_m) / direct


def lateral_velocity_stats(t_s: Sequence[float], y_m: Sequence[float]) -> dict[str, float]:
    """Lateral-speed statistics derived from sampled positions."""
    if len(t_s) != len(y_m) or len(t_s) < 2:
        raise ValueError("t_s and y_m must have equal length >= 2")
    vy: list[float] = []
    for i in range(1, len(t_s)):
        dt = t_s[i] - t_s[i - 1]
        if dt <= 0:
            raise ValueError("timestamps must be strictly increasing")
        vy.append((y_m[i] - y_m[i - 1]) / dt)
    return {
        "mean_abs_vy_mps": fmean(abs(v) for v in vy),
        "sd_vy_mps": pstdev(vy) if len(vy) > 1 else 0.0,
        "max_abs_vy_mps": max(abs(v) for v in vy),
    }


def hard_braking_rate(accel_mps2: Sequence[float], threshold_mps2: float = -3.0) -> float:
    """Share of samples at/below a configurable braking threshold."""
    if not accel_mps2:
        raise ValueError("accel_mps2 cannot be empty")
    if threshold_mps2 >= 0:
        raise ValueError("threshold_mps2 must be negative")
    return sum(a <= threshold_mps2 for a in accel_mps2) / len(accel_mps2)
