import pytest

from roadspacelab.capacity import (
    finite_length_change_gain,
    flow_from_time_headway,
    interpret_dynamic_area_claim,
    kmh_to_mps,
    length_capacity_elasticity_constant_gap,
    productive_person_throughput,
    queue_slots_1d,
    side_by_side_count,
)


def test_88m2_area_claim_does_not_define_unique_flow_without_speed():
    at_30 = interpret_dynamic_area_claim(88.0, 3.5, kmh_to_mps(30.0))
    at_50 = interpret_dynamic_area_claim(88.0, 3.5, kmh_to_mps(50.0))

    assert at_30.space_headway_m == pytest.approx(25.142857, rel=1e-6)
    assert at_30.flow_vph_per_stream == pytest.approx(1193.18, rel=1e-4)
    assert at_50.flow_vph_per_stream == pytest.approx(1988.64, rel=1e-4)
    assert at_50.flow_vph_per_stream > at_30.flow_vph_per_stream


def test_positive_gap_makes_length_capacity_elasticity_less_than_one():
    epsilon = length_capacity_elasticity_constant_gap(4.0, 12.0)
    assert epsilon == pytest.approx(0.25)
    assert 0.0 < epsilon < 1.0


def test_ten_percent_shorter_car_gives_only_about_2_56pct_gain_with_12m_gap():
    gain = finite_length_change_gain(
        kmh_to_mps(30.0), 4.0, 3.6, gap_m=12.0
    )
    assert 100.0 * gain == pytest.approx(2.56410256, rel=1e-6)


def test_vehicle_length_has_zero_effect_when_time_headway_is_empirically_fixed():
    # Vehicle length is intentionally absent from q=3600/h.
    before = flow_from_time_headway(1.9)
    after = flow_from_time_headway(1.9)
    assert after == before


def test_small_width_change_can_have_zero_parallelism_gain_until_threshold():
    before = side_by_side_count(3.5, effective_vehicle_width_m=1.80, lateral_gap_m=0.40)
    after = side_by_side_count(3.5, effective_vehicle_width_m=1.62, lateral_gap_m=0.40)
    assert before == 1
    assert after == 1


def test_stopped_queue_is_much_more_sensitive_to_gap_assumption():
    tight = queue_slots_1d(100.0, vehicle_length_m=4.0, gap_m=0.5)
    loose = queue_slots_1d(100.0, vehicle_length_m=4.0, gap_m=1.5)
    assert tight == 22
    assert loose == 18


def test_productive_share_keeps_empty_commercial_movement_separate():
    # 2000 veh/h, 1.5 persons per occupied vehicle, 40% of vehicle flow empty.
    assert productive_person_throughput(2000, 1.5, 0.60) == pytest.approx(1800)
