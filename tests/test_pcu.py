import pytest

from roadspacelab.pcu import (
    IRC_SP41_REPORTED_FIXED_PCU,
    alex_isaac_2015_saturated_pcu,
    pcu_weighted_flow,
)


NORMAL_MIX = {
    "two_wheeler": 0.40,
    "three_wheeler": 0.20,
    "car": 0.30,
    "bus": 0.10,
}


def test_reproduces_published_saturation_regression_at_example_mix():
    result = alex_isaac_2015_saturated_pcu(
        NORMAL_MIX,
        speed_kmh=25.0,
        approach_width_m=7.0,
    )

    assert result["two_wheeler"] == pytest.approx(0.1718)
    assert result["three_wheeler"] == pytest.approx(0.4494)
    assert result["car"] == pytest.approx(1.0460)
    assert result["bus"] == pytest.approx(3.4060)


def test_dynamic_baseline_is_not_the_same_as_legacy_fixed_table():
    result = alex_isaac_2015_saturated_pcu(
        NORMAL_MIX,
        speed_kmh=25.0,
        approach_width_m=7.0,
    )
    assert result["two_wheeler"] != pytest.approx(IRC_SP41_REPORTED_FIXED_PCU["two_wheeler"])
    assert result["three_wheeler"] != pytest.approx(IRC_SP41_REPORTED_FIXED_PCU["three_wheeler"])


def test_scope_guard_rejects_using_signal_model_as_universal_model():
    with pytest.raises(ValueError, match="outside"):
        alex_isaac_2015_saturated_pcu(
            NORMAL_MIX,
            speed_kmh=45.0,
            approach_width_m=7.0,
        )

    with pytest.raises(ValueError, match="outside"):
        alex_isaac_2015_saturated_pcu(
            NORMAL_MIX,
            speed_kmh=25.0,
            approach_width_m=14.0,
        )


def test_composition_must_sum_to_one():
    bad_mix = dict(NORMAL_MIX)
    bad_mix["bus"] = 0.20
    with pytest.raises(ValueError, match="sum to 1"):
        alex_isaac_2015_saturated_pcu(
            bad_mix,
            speed_kmh=25.0,
            approach_width_m=7.0,
        )


def test_weighted_flow_is_explicit_accounting():
    fixed = {
        "two_wheeler": 0.30,
        "three_wheeler": 0.40,
        "car": 1.0,
        "bus": 2.8,
    }
    flows = {
        "two_wheeler": 400,
        "three_wheeler": 200,
        "car": 300,
        "bus": 100,
    }
    assert pcu_weighted_flow(flows, fixed) == pytest.approx(780.0)
