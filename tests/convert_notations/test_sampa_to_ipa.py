import pytest  # type: ignore
from convert_pa.convert_notations import sampa_to_ipa


def test_sampa_to_ipa_basic():
    # Example: '""On$d@$%lE*u0s' should convert to IPA (Åndeløs)
    sampa = '""On$d@$%lE*u0s'
    ipa = sampa_to_ipa(sampa)
    # The expected IPA string depends on the mapping, but should not raise or be empty
    assert isinstance(ipa, str)
    assert ipa != ""


def test_sampa_to_ipa_invalid_segment():
    # Should exit if an unknown segment is present
    sampa = "invalidsegment"
    with pytest.raises(ValueError) as excinfo:
        sampa_to_ipa(sampa)
    assert "invalidsegment" in str(excinfo.value)


def test_sampa_to_ipa_multiple_segments():
    # Test with several valid segments
    sampa = "d@$lE"
    ipa = sampa_to_ipa(sampa)
    assert isinstance(ipa, str)
    assert ipa != ""


def test_sampa_to_ipa_empty_string():
    # Should return empty string for empty input
    assert sampa_to_ipa("") == ""


def test_sampa_to_ipa_whitespace_handled_gracefully():
    # Should handle input with extra whitespace gracefully
    sampa = "d@ $ lE "
    ipa = sampa_to_ipa(sampa)
    assert isinstance(ipa, str)
    assert ipa != ""
