"""Transparent baseline road-space and traffic metrics.

These functions deliberately expose assumptions. They are reference baselines,
not a claim that heterogeneous traffic can be reduced to one scalar.
"""
from __future__ import annotations

import math


def _positive(name: str, value: float) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be > 0")


def static_footprint(length_m: float, width_m: float) -> float:
    """Projected physical vehicle area in square metres."""
    _positive("length_m", length_m)
    _positive("width_m", width_m)
    return length_m * width_m


def queue_storage(segment_length_m: float, vehicle_length_m: float, standstill_gap_m: float) -> int:
    """Whole vehicles fitting in a stationary single-file queue approximation."""
    _positive("segment_length_m", segment_length_m)
    _positive("vehicle_length_m", vehicle_length_m)
    if standstill_gap_m < 0:
        raise ValueError("standstill_gap_m must be >= 0")
    return math.floor(segment_length_m / (vehicle_length_m + standstill_gap_m))


def flow_from_headway(headway_s: float) -> float:
    """Theoretical vehicles/hour from an observed mean time headway."""
    _positive("headway_s", headway_s)
    return 3600.0 / headway_s


def signal_capacity(headway_s: float, green_s: float, cycle_s: float, lanes: int = 1) -> float:
    """Saturation-flow × effective-green approximation, veh/hour."""
    _positive("headway_s", headway_s)
    _positive("green_s", green_s)
    _positive("cycle_s", cycle_s)
    if green_s > cycle_s:
        raise ValueError("green_s cannot exceed cycle_s")
    if lanes < 1:
        raise ValueError("lanes must be >= 1")
    return flow_from_headway(headway_s) * (green_s / cycle_s) * lanes


def stopping_distance(speed_mps: float, reaction_s: float, decel_mps2: float) -> float:
    """Reaction distance plus constant-deceleration braking distance."""
    if speed_mps < 0 or reaction_s < 0:
        raise ValueError("speed_mps and reaction_s must be >= 0")
    _positive("decel_mps2", decel_mps2)
    return speed_mps * reaction_s + speed_mps**2 / (2.0 * decel_mps2)


def differential_safe_gap(
    speed_mps: float,
    reaction_s: float,
    follower_decel_mps2: float,
    leader_decel_mps2: float,
    reserve_m: float = 0.0,
) -> float:
    """Illustrative gap when leader and follower may brake differently.

    Not a calibrated Indian-driving model. It is included so the simplifying
    assumptions can be tested against observed trajectories rather than hidden.
    """
    if speed_mps < 0 or reaction_s < 0 or reserve_m < 0:
        raise ValueError("speed_mps, reaction_s and reserve_m must be >= 0")
    _positive("follower_decel_mps2", follower_decel_mps2)
    _positive("leader_decel_mps2", leader_decel_mps2)
    follower_brake = speed_mps**2 / (2.0 * follower_decel_mps2)
    leader_brake = speed_mps**2 / (2.0 * leader_decel_mps2)
    return speed_mps * reaction_s + max(0.0, follower_brake - leader_brake) + reserve_m


def person_throughput(vehicle_flow_vph: float, mean_occupancy: float) -> float:
    """Persons/hour. Occupancy is deliberately separate from vehicle capacity."""
    if vehicle_flow_vph < 0 or mean_occupancy < 0:
        raise ValueError("vehicle_flow_vph and mean_occupancy must be >= 0")
    return vehicle_flow_vph * mean_occupancy


def deadheading_multiplier(empty_vkt_share: float) -> float:
    """Total vehicle-km per occupied vehicle-km implied by empty-VKT share."""
    if not 0 <= empty_vkt_share < 1:
        raise ValueError("empty_vkt_share must be in [0, 1)")
    return 1.0 / (1.0 - empty_vkt_share)


def road_space_time(dynamic_area_m2: float, duration_s: float) -> float:
    """Road-Space-Time (RST) in m²·s for a constant-area interval."""
    if dynamic_area_m2 < 0 or duration_s < 0:
        raise ValueError("dynamic_area_m2 and duration_s must be >= 0")
    return dynamic_area_m2 * duration_s


def useful_mobility_efficiency(passenger_km: float, road_space_time_m2s: float) -> float:
    """Passenger-km per m²·s of road-space-time."""
    if passenger_km < 0:
        raise ValueError("passenger_km must be >= 0")
    _positive("road_space_time_m2s", road_space_time_m2s)
    return passenger_km / road_space_time_m2s


def capacity_area_elasticity(
    capacity_before: float,
    capacity_after: float,
    area_before_m2: float,
    area_after_m2: float,
) -> float:
    """Capacity response per proportional physical-area reduction.

    E = ((C_after-C_before)/C_before) / ((A_before-A_after)/A_before).
    E=1 means a 10% physical-area reduction accompanies a 10% capacity gain.
    """
    _positive("capacity_before", capacity_before)
    if capacity_after < 0:
        raise ValueError("capacity_after must be >= 0")
    _positive("area_before_m2", area_before_m2)
    _positive("area_after_m2", area_after_m2)
    area_reduction = (area_before_m2 - area_after_m2) / area_before_m2
    if area_reduction == 0:
        raise ValueError("area_before_m2 and area_after_m2 must differ")
    capacity_change = (capacity_after - capacity_before) / capacity_before
    return capacity_change / area_reduction
