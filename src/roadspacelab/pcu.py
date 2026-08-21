"""Published PCU/PCE baselines used by Road Space Lab.

These functions reproduce published models for comparison.  They are not Road
Space Lab recommendations and must not be extrapolated outside their stated
calibration regime without validation.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


# Values reported by Alex & Isaac (2015) as IRC SP:41 recommendations.
# Kept only as a legacy fixed-PCU baseline; Road Space Lab has not independently
# re-derived these values from IRC SP:41 in this module.
IRC_SP41_REPORTED_FIXED_PCU = {
    "two_wheeler": 0.30,
    "three_wheeler": 0.40,
    "car": 1.00,
    "bus_lorry": 2.80,
}


@dataclass(frozen=True, slots=True)
class PCUModelCard:
    name: str
    source: str
    doi: str
    facility: str
    geography: str
    regime: str
    width_range_m: tuple[float, float]
    speed_range_kmh: tuple[float, float]
    notes: str


ALEX_ISAAC_2015_SATURATED = PCUModelCard(
    name="Alex & Isaac 2015 dynamic PCU — saturation model",
    source="Dynamic PCU Values at Signalised Intersections in India for Mixed Traffic",
    doi="10.7708/ijtte.2015.5(2).09",
    facility="four-legged signalised intersection approaches on level stretches",
    geography="India",
    regime="saturated mixed traffic; model developed using TRAFFICSIM",
    width_range_m=(3.5, 10.5),
    speed_range_kmh=(0.0, 30.0),
    notes=(
        "Published regression model. Inputs are traffic-class proportions, stream "
        "speed in km/h and approach width in metres. Use as a reproducible baseline, "
        "not as a universal PCU table."
    ),
)


_REQUIRED_CLASSES = ("two_wheeler", "three_wheeler", "car", "bus")


def _validate_composition(composition: Mapping[str, float]) -> tuple[float, float, float, float]:
    missing = [name for name in _REQUIRED_CLASSES if name not in composition]
    if missing:
        raise ValueError(f"missing composition classes: {missing}")

    values = tuple(float(composition[name]) for name in _REQUIRED_CLASSES)
    if any(value < 0 or value > 1 for value in values):
        raise ValueError("vehicle-class proportions must each be in [0, 1]")
    if abs(sum(values) - 1.0) > 1e-6:
        raise ValueError("vehicle-class proportions must sum to 1")
    return values  # type: ignore[return-value]


def alex_isaac_2015_saturated_pcu(
    composition: Mapping[str, float],
    *,
    speed_kmh: float,
    approach_width_m: float,
    strict_scope: bool = True,
) -> dict[str, float]:
    """Reproduce the saturated dynamic-PCU regressions in Alex & Isaac (2015).

    Published equations (Table 1) are evaluated directly.  `strict_scope=True`
    rejects speed/width inputs outside the paper's stated experiment scope so a
    convenient baseline does not silently turn into a universal model.

    Returns PCU estimates for two-wheelers, three-wheelers, cars and buses.
    """
    tw, three, car, bus = _validate_composition(composition)
    speed = float(speed_kmh)
    width = float(approach_width_m)

    if speed <= 0:
        raise ValueError("speed_kmh must be > 0")
    if width <= 0:
        raise ValueError("approach_width_m must be > 0")

    if strict_scope:
        if not (3.5 <= width <= 10.5):
            raise ValueError("approach_width_m is outside the published 3.5–10.5 m scope")
        if speed > 30.0:
            raise ValueError("speed_kmh is outside the paper's saturated-regime scope (<=30 km/h)")

    return {
        "two_wheeler": (
            0.525
            - 0.181 * tw
            - 0.409 * three
            - 0.48 * car
            - 0.57 * bus
            - 0.003 * speed
            + 0.011 * width
        ),
        "three_wheeler": (
            2.251
            - 1.839 * tw
            - 1.69 * three
            - 2.18 * car
            - 2.09 * bus
            - 0.003 * speed
            + 0.03 * width
        ),
        "car": (
            3.003
            - 2.61 * tw
            - 2.48 * three
            - 2.59 * car
            - 2.45 * bus
            + 0.006 * speed
            + 0.065 * width
        ),
        "bus": (
            -2.313
            + 1.995 * tw
            + 1.81 * three
            + 2.19 * car
            + 5.32 * bus
            + 0.083 * speed
            + 0.185 * width
        ),
    }


def pcu_weighted_flow(vehicle_flows_vph: Mapping[str, float], pcu: Mapping[str, float]) -> float:
    """Convert class vehicle flows to PCU/hour using an explicit PCU mapping."""
    total = 0.0
    for vehicle_class, flow in vehicle_flows_vph.items():
        if flow < 0:
            raise ValueError("vehicle flows must be >= 0")
        if vehicle_class not in pcu:
            raise ValueError(f"no PCU value supplied for class {vehicle_class!r}")
        total += float(flow) * float(pcu[vehicle_class])
    return total
