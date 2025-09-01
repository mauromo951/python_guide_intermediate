#ejecutar test, python -m pytest
import pytest
from pytest_27.main import suma, is_bigger
 

def test_suma():
    assert suma(2,5) == 7

def test_is_bigger():
    assert is_bigger(10,11)

#Decorador
@pytest.mark.parametrize(
        "input_x, input_y,expected",
        [
            (5,1,6),
            (suma(2,2),4,8),
        ]
)
def test_sum_params(input_x, input_y,expected):
    assert suma(input_x,input_y) == expected