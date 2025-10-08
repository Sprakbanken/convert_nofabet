import pytest
from convert_pa.convert_notations import convert_nofabet_trans


def test_convert_nofabet_trans_to_sampa_basic():
    # "Billighetserstatningens"
    nofabet = "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S"
    expected_sampa = '""bI$lI$he:t$s{r$%stAt$nIN$g@ns'
    result = convert_nofabet_trans(nofabet, to="sampa")
    assert result == expected_sampa


def test_convert_nofabet_trans_to_ipa_basic():
    # "Billighetserstatningens"
    nofabet = "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S"
    expected_ipa = '"bɪ.lɪ.heːt.sær.ˌstɑt.nɪŋ.gəns'
    result = convert_nofabet_trans(nofabet, to="ipa")
    assert result == expected_ipa


def test_convert_nofabet_trans_invalid_standard():
    nofabet = "B IH2 L IH0"
    with pytest.raises(ValueError) as excinfo:
        convert_nofabet_trans(nofabet, to="unknown")
    assert "unknown notation" in str(excinfo.value)


def test_convert_nofabet_trans_empty_input_gives_empty_output():
    assert convert_nofabet_trans("", to="sampa") == ""
    assert convert_nofabet_trans("", to="ipa") == ""


def test_convert_nofabet_trans_single_syllable():
    nofabet = "B IH2"
    # Should convert just one syllable
    sampa = convert_nofabet_trans(nofabet, to="sampa")
    ipa = convert_nofabet_trans(nofabet, to="ipa")
    assert isinstance(sampa, str)
    assert isinstance(ipa, str)
    assert sampa != ""
    assert ipa != ""


def test_convert_nofabet_trans_multiple_syllables_get_syllable_boundaries():
    nofabet = "B IH2 L IH0"
    sampa = convert_nofabet_trans(nofabet, to="sampa")
    ipa = convert_nofabet_trans(nofabet, to="ipa")
    assert "$" in sampa
    assert "." not in sampa
    assert "." in ipa
    assert "$" not in ipa


@pytest.mark.parametrize("text_with_space", [" B IH2 L IH0", "B IH2 L IH0 "])
def test_trailing_whitespaces_get_trimmed(text_with_space):
    result = convert_nofabet_trans(text_with_space, to="ipa")
    assert isinstance(result, str)
