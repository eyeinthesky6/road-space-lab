"""Transparent capacity formulas for Road Space Lab.

The point of this module is not to collapse traffic into one magic number.  It
provides explicit boundary models whose assumptions can be replaced by observed
trajectory data.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


def _positive(name: str, value: float) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be > 0")


def _non_negative(name: str, value: float) -> None:
    if value < 0:
        raise ValueError(f"{name} must be >= 0")


def kmh_to_mps(speed_kmh: float) -> float:
    _non_negative("speed_kmh", speed_kmh)
    return speed_kmh / 3.6


def queue_slots_1d(segment_length_m: float, vehicle_length_m: float, gap_m: float) -> int:
    """Maximum whole vehicles in a regular single-file stopped queue.

    Solves n*L + (n-1)*g <= S, hence floor((S+g)/(L+g)).  Real mixed queues can
    stagger and interleave; this is a transparent geometric baseline only.
    """
    _positive("segment_length_m", segment_length_m)
    _positive("vehicle_length_m", vehicle_length_m)
    _non_negative("gap_m", gap_m)
    return math.floor((segment_length_m + gap_m) / (vehicle_length_m + gap_m))


def side_by_side_count(
    carriageway_width_m: float,
    effective_vehicle_width_m: float,
    lateral_gap_m: float = 0.0,
) -> int:
    """Regular-grid lateral packing count.

    `effective_vehicle_width_m` may be a marked-lane allocation, an empirically
    measured dynamic envelope, or a physical width.  Those are different models
    and must be labelled as such.
    """
    _positive("carriageway_width_m", carriageway_width_m)
    _positive("effective_vehicle_width_m", effective_vehicle_width_m)
    _non_negative("lateral_gap_m", lateral_gap_m)
    return math.floor(
        (carriageway_width_m + lateral_gap_m)
        / (effective_vehicle_width_m + lateral_gap_m)
    )


def flow_from_time_headway(headway_s: float) -> float:
    """Single-stream vehicles/hour from front-to-front time headway."""
    _positive("headway_s", headway_s)
    return 3600.0 / headway_s


def flow_from_constant_distance_gap(
    speed_mps: float,
    vehicle_length_m: float,
    gap_m: float,
) -> float:
    """Single-stream veh/h if drivers hold a fixed distance gap at fixed speed.

    q = 3600*v/(L+g).  This is a boundary model, not a universal car-following
    law.  It is useful because it makes the effect of vehicle length explicit.
    """
    _positive("speed_mps", speed_mps)
    _positive("vehicle_length_m", vehicle_length_m)
    _non_negative("gap_m", gap_m)
    return 3600.0 * speed_mps / (vehicle_length_m + gap_m)


def length_capacity_elasticity_constant_gap(vehicle_length_m: float, gap_m: float) -> float:
    """Local capacity elasticity to a proportional reduction in vehicle length.

    For q=v/(L+g), epsilon_L = L/(L+g).  Therefore any positive non-vehicle gap
    makes the longitudinal capacity response smaller than the length reduction.
    """
    _positive("vehicle_length_m", vehicle_length_m)
    _non_negative("gap_m", gap_m)
    return vehicle_length_m / (vehicle_length_m + gap_m)


def finite_length_change_gain(
    speed_mps: float,
    length_before_m: float,
    length_after_m: float,
    gap_m: float,
) -> float:
    """Fractional flow change under the constant-distance-gap boundary model."""
    _positive("length_before_m", length_before_m)
    _positive("length_after_m", length_after_m)
    before = flow_from_constant_distance_gap(speed_mps, length_before_m, gap_m)
    after = flow_from_constant_distance_gap(speed_mps, length_after_m, gap_m)
    return (after - before) / before


def multistream_capacity(
    single_stream_flow_vph: float,
    parallel_streams: int,
    green_ratio: float = 1.0,
) -> float:
    """Simple cross-section capacity from stream flow, parallelism and green share."""
    _non_negative("single_stream_flow_vph", single_stream_flow_vph)
    if parallel_streams < 1:
        raise ValueError("parallel_streams must be >= 1")
    if not 0 <= green_ratio <= 1:
        raise ValueError("green_ratio must be in [0, 1]")
    return single_stream_flow_vph * parallel_streams * green_ratio


def dynamic_slot_area_from_headway(
    speed_mps: float,
    headway_s: float,
    effective_lateral_width_m: float,
) -> float:
    """Area of a moving front-to-front slot: (v*h) * effective width, m².

    Effective width must be defined by the analysis: lane allocation, observed
    territory, or an interaction envelope.  Physical body width is not assumed.
    """
    _positive("speed_mps", speed_mps)
    _positive("headway_s", headway_s)
    _positive("effective_lateral_width_m", effective_lateral_width_m)
    return speed_mps * headway_s * effective_lateral_width_m


@dataclass(frozen=True, slots=True)
class AreaClaimInterpretation:
    area_m2: float
    allocated_width_m: float
    space_headway_m: float
    speed_mps: float
    time_headway_s: float
    flow_vph_per_stream: float


def interpret_dynamic_area_claim(
    area_m2: float,
    allocated_width_m: float,
    speed_mps: float,
) -> AreaClaimInterpretation:
    """Reverse-engineer an 'X m² per moving vehicle' claim.

    If area is interpreted as allocated width x front-to-front longitudinal slot,
    the same area implies different time headways/capacities at different speeds.
    This exposes why area alone is not a complete moving-capacity specification.
    """
    _positive("area_m2", area_m2)
    _positive("allocated_width_m", allocated_width_m)
    _positive("speed_mps", speed_mps)
    space_headway = area_m2 / allocated_width_m
    time_headway = space_headway / speed_mps
    return AreaClaimInterpretation(
        area_m2=area_m2,
        allocated_width_m=allocated_width_m,
        space_headway_m=space_headway,
        speed_mps=speed_mps,
        time_headway_s=time_headway,
        flow_vph_per_stream=flow_from_time_headway(time_headway),
    )


def productive_person_throughput(
    vehicle_flow_vph: float,
    mean_occupancy: float,
    productive_share: float = 1.0,
) -> float:
    """Beneficiary persons/hour after an explicit productive/occupied share.

    For a private occupied trip, productive_share is normally 1.  For a taxi/fleet
    stream, empty cruising or repositioning can be represented explicitly rather
    than silently counted as passenger movement.
    """
    _non_negative("vehicle_flow_vph", vehicle_flow_vph)
    _non_negative("mean_occupancy", mean_occupancy)
    if not 0 <= productive_share <= 1:
        raise ValueError("productive_share must be in [0, 1]")
    return vehicle_flow_vph * mean_occupancy * productive_share
