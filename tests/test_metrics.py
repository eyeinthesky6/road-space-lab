import pytest

from roadspacelab.metrics import (
    capacity_area_elasticity,
    deadheading_multiplier,
    differential_safe_gap,
    flow_from_headway,
    person_throughput,
    queue_storage,
    signal_capacity,
    static_footprint,
)
from roadspacelab.trajectory import lateral_excursion, path_tortuosity


def test_queue_storage_example():
    assert queue_storage(100, 4.0, 1.5) == 18
    assert queue_storage(100, 3.6, 1.5) == 19


def test_headway_and_signal():
    assert flow_from_headway(2.0) == 1800
    assert signal_capacity(2.0, 30, 60) == 900


def test_deadheading_and_person_throughput():
    assert deadheading_multiplier(0.5) == 2.0
    assert person_throughput(1000, 1.5) == 1500


def test_area_and_differential_gap():
    assert static_footprint(4, 1.8) == pytest.approx(7.2)
    assert differential_safe_gap(10, 1, 5, 5, reserve_m=1) == pytest.approx(11)


def test_capacity_elasticity():
    assert capacity_area_elasticity(1000, 1050, 10, 9) == pytest.approx(0.5)


def test_lateral_metrics():
    y = [0, .1, -.1, .2, -.2, 0]
    assert lateral_excursion(y) > 0
    assert path_tortuosity([0, 1, 2, 3, 4, 5], y) >= 1
