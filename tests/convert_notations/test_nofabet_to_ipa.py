import pytest
from convert_pa.convert_notations import nofabet_to_ipa


def test_basic_conversion():
    # "Billighetserstatningens"
    nofabet = "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S"
    expected_ipa = '"bɪ.lɪ.heːt.sær.ˌstɑt.nɪŋ.gəns'
    result = nofabet_to_ipa(nofabet)
    assert result == expected_ipa


def test_empty_input_returns_empty_output():
    input_trans = ""
    result = nofabet_to_ipa(input_trans)
    assert result == ""


def test_invalid_symbol():
    input_trans = "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S XX"
    with pytest.raises(KeyError):
        nofabet_to_ipa(input_trans)
