"""Reproduce the first Road Space Lab vehicle-size falsification checks.

Run after `pip install -e .`:
    python examples/debunk_vehicle_size.py
"""
from roadspacelab.capacity import (
    finite_length_change_gain,
    flow_from_time_headway,
    interpret_dynamic_area_claim,
    kmh_to_mps,
    length_capacity_elasticity_constant_gap,
    queue_slots_1d,
    side_by_side_count,
)


print("1) What does '88 m² per moving car' actually imply?")
for speed_kmh in (20, 30, 40, 50):
    r = interpret_dynamic_area_claim(88.0, 3.5, kmh_to_mps(speed_kmh))
    print(
        f"  {speed_kmh:>2} km/h -> space headway {r.space_headway_m:5.2f} m, "
        f"time headway {r.time_headway_s:4.2f} s, "
        f"flow {r.flow_vph_per_stream:7.1f} veh/h/stream"
    )

print("\n2) A 10% shorter car: moving constant-gap boundary")
gain = finite_length_change_gain(kmh_to_mps(30), 4.0, 3.6, gap_m=12.0)
epsilon = length_capacity_elasticity_constant_gap(4.0, 12.0)
print(f"  local length elasticity = {epsilon:.3f}")
print(f"  4.0 m -> 3.6 m capacity gain = {100*gain:.2f}% (not 10%)")

print("\n3) Same 10% shorter car: observed time-headway boundary")
q_before = flow_from_time_headway(1.9)
q_after = flow_from_time_headway(1.9)
print(f"  at fixed observed h=1.9 s: {q_before:.1f} -> {q_after:.1f} veh/h (0% gain)")

print("\n4) Width is threshold-driven")
p_before = side_by_side_count(3.5, 1.80, 0.40)
p_after = side_by_side_count(3.5, 1.62, 0.40)
print(f"  3.5 m cross-section: 1.80 m -> 1.62 m effective width gives {p_before} -> {p_after} streams")

print("\n5) Standstill queue is more geometry-sensitive")
for gap in (0.5, 0.8, 1.0, 1.5):
    normal = queue_slots_1d(100.0, 4.0, gap)
    shorter = queue_slots_1d(100.0, 3.6, gap)
    print(f"  gap={gap:3.1f} m: 4.0 m car={normal:2d}, 3.6 m car={shorter:2d}")

print("\nInterpretation: these are boundary models, not empirical conclusions. SPT Chennai is the first trajectory test.")
