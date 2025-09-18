#Parametrize

import pytest

def sumar(a, b):
    return a + b

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
    ]
)
def test_sumar(a, b, esperado):
    assert sumar(a, b) == esperado
