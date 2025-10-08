import pytest  # type: ignore
from convert_pa.phonetic_inventory import is_valid_ons_cluster


@pytest.mark.xfail
def test_is_valid_ons_cluster_valid_cases():
    """TODO: fix issue where NJ is not a valid onset"""
    # Valid 2-phone clusters
    assert is_valid_ons_cluster(["N", "J"])  # nasal + j
    assert is_valid_ons_cluster(["M", "J"])  # nasal + j
    assert is_valid_ons_cluster(["P", "L"])  # P + liquid
    assert is_valid_ons_cluster(["B", "L"])  # B + liquid
    assert is_valid_ons_cluster(["T", "R"])  # T + R
    assert is_valid_ons_cluster(["D", "J"])  # D + J
    assert is_valid_ons_cluster(["RT", "R"])  # retroflex plosive + R
    assert is_valid_ons_cluster(["K", "L"])  # K + liquid
    assert is_valid_ons_cluster(["K", "N"])  # K + N
    assert is_valid_ons_cluster(["K", "V"])  # K + v
    assert is_valid_ons_cluster(["G", "L"])  # G + liquid
    assert is_valid_ons_cluster(["G", "N"])  # G + N
    assert is_valid_ons_cluster(["F", "L"])  # F + liquid
    assert is_valid_ons_cluster(["F", "J"])  # F + J
    assert is_valid_ons_cluster(["F", "N"])  # F + N
    assert is_valid_ons_cluster(["S", "N"])  # S + nasal
    assert is_valid_ons_cluster(["S", "L"])  # S + L
    assert is_valid_ons_cluster(["S", "V"])  # S + v
    assert is_valid_ons_cluster(["S", "K"])  # S + unvoiced plosive
    assert is_valid_ons_cluster(["SJ", "T"])  # SJ + unvoiced plosive
    assert is_valid_ons_cluster(["RS", "P"])  # RS + unvoiced plosive
    assert is_valid_ons_cluster(["V", "R"])  # v + R

    # Valid 3-phone clusters
    assert is_valid_ons_cluster(["S", "P", "L"])  # S + P + L
    assert is_valid_ons_cluster(["SJ", "P", "L"])  # SJ + P + L
    assert is_valid_ons_cluster(["RS", "P", "R"])  # RS + P + R
    assert is_valid_ons_cluster(["S", "T", "R"])  # S + T + R
    assert is_valid_ons_cluster(["S", "K", "L"])  # S + K + L
    assert is_valid_ons_cluster(["SJ", "K", "R"])  # SJ + K + R
    assert is_valid_ons_cluster(["S", "G", "V"])  # S + G + V


def test_is_valid_ons_cluster_invalid_cases():
    # Invalid clusters
    assert not is_valid_ons_cluster(["L", "N"])
    assert not is_valid_ons_cluster(["K", "K"])
    assert not is_valid_ons_cluster(["S", "S"])
    assert not is_valid_ons_cluster(["A", "J"])
    assert not is_valid_ons_cluster(["S", "P", "N"])
    assert not is_valid_ons_cluster(["N"])  # single phone
    assert not is_valid_ons_cluster([])  # empty list
    assert not is_valid_ons_cluster(["S"])  # single phone
    assert not is_valid_ons_cluster(["S", "A"])  # S + vowel
    assert not is_valid_ons_cluster(["K", "R", "L"])  # not a valid 3-phone cluster
