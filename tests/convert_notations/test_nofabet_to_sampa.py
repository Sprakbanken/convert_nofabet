import pytest
from convert_pa.convert_notations import nofabet_to_sampa


def test_basic_conversion():
    nofabet_trans = "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S"
    sampa_trans = '""bI$lI$he:t$s{r$%stAt$nIN$g@ns'
    result = nofabet_to_sampa(nofabet_trans)
    assert isinstance(result, str)
    assert len(result) > 0
    assert result == sampa_trans


def test_empty_input_returns_empty_output():
    input_trans = ""
    result = nofabet_to_sampa(input_trans)
    assert result == ""


def test_invalid_symbol():
    input_trans = "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S XX"
    with pytest.raises(KeyError):
        nofabet_to_sampa(input_trans)
