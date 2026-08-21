from io import StringIO

import pytest

from roadspacelab.spt import group_by_vehicle, iter_spt


HEADER = "New_TimeStamp,Vehicle_ID,Vehicle_class,Length,Width,Long_smooth,v_smooth,a_smooth,Latright_smooth,vy_smooth,ay_smooth\n"


def test_spt_adapter_normalizes_published_schema():
    data = HEADER + "0.1,42,0,1.9,0.7,12.0,5.0,-0.4,2.1,0.2,0.1\n"
    point = next(iter_spt(StringIO(data)))
    assert point.dataset == "SPT-Chennai"
    assert point.vehicle_id == "42"
    assert point.vehicle_class == "two_wheeler"
    assert point.x_m == pytest.approx(12.0)
    assert point.y_m == pytest.approx(2.1)
    assert point.velocity_lat_mps == pytest.approx(0.2)


def test_grouping_sorts_trajectory_by_time():
    data = HEADER + (
        "0.2,7,1,4.0,1.7,11,4,0,2,0,0\n"
        "0.1,7,1,4.0,1.7,10,4,0,2,0,0\n"
    )
    grouped = group_by_vehicle(iter_spt(StringIO(data)))
    assert [p.timestamp_s for p in grouped["7"]] == [0.1, 0.2]


def test_missing_columns_fail_loudly():
    with pytest.raises(ValueError, match="missing required columns"):
        list(iter_spt(StringIO("Vehicle_ID,Vehicle_class\n1,1\n")))
