from joblib.testing import raises
from prompt_toolkit.validation import ValidationError

from ReadFileCSV.CSV_Read import Expenses_Mean
import pytest
from _pytest.outcomes import Failed

@pytest.mark.parametrize("a,b,expected_result", [(10, 2, 5),
                                                 (20, 10, 2),
                                                 (30, -5, -6),
                                                 (-5, -2, 2.5)])
def test_division_positive(a, b, expected_result):
    assert Expenses_Mean(a, b) == expected_result

def test_zero_division():
    assert Expenses_Mean(var1=5,var2=0) == None

def test_type_error():
    with pytest.raises(TypeError):
        Expenses_Mean(10,"5")



