import pytest  # type: ignore
from convert_pa.convert_notations import nofabet_to_syllables
import convert_pa.convert_notations as cn


@pytest.fixture(autouse=True)
def mock_phones_and_cluster(monkeypatch):
    cn.PHONES_NOFABET = {
        "nuclei": [
            "AA",
            "AE",
            "II",
            "IH",
            "EE",
            "EH",
            "AEH",
            "AH",
            "AX",
            "OO",
            "OH",
            "OA",
            "OAH",
            "OE",
            "OEH",
            "UU",
            "UH",
            "YY",
        ],
        "single_onsets": ["B", "L", "H", "T", "S", "R", "G", "N"],
        "ng": ["NG"],
        "consonants": ["B", "L", "H", "T", "S", "R", "G", "N", "NG"],
    }
    monkeypatch.setattr(cn, "is_valid_ons_cluster", lambda segs: False)


def test_single_syllable():
    transcription = "B IH2"
    expected = [["B", "IH2"]]
    result = nofabet_to_syllables(transcription)
    assert result == expected


def test_multiple_syllables():
    transcription = "B IH2 L IH0"
    expected = [["B", "IH2"], ["L", "IH0"]]
    result = nofabet_to_syllables(transcription)
    assert result == expected


def test_with_ng_between_nuclei():
    transcription = "AH3 NG IH0"
    expected = [["AH3", "NG"], ["IH0"]]
    result = nofabet_to_syllables(transcription)
    assert result == expected


def test_with_underscore():
    transcription = "B IH2 _ L IH0"
    expected = [["B", "IH2", "_"], ["L", "IH0"]]
    result = nofabet_to_syllables(transcription)
    assert result == expected


@pytest.mark.xfail
def test_complex_example():
    """TODO: Fix issue with syllable boundary where S is chosen as onset"""
    transcription = "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG AX0 N S"
    expected = [
        ["B", "IH2"],
        ["L", "IH0"],
        ["H", "EE0", "T", "S"],
        ["AEH0", "R"],
        ["S", "T", "AH3", "T"],
        ["N", "IH0", "NG"],
        ["AX0", "N", "S"],
    ]
    result = nofabet_to_syllables(transcription)
    assert result == expected


def test_empty_input_returns_empty_output():
    input_trans = ""
    result = nofabet_to_syllables(input_trans)
    assert result == []
