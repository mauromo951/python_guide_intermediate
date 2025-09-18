#Parametrize, ejecuta un mismo test con varios valores.

#Ejecutar pytest para un archivo en particular python -m pytest -v .\parametrize_01.py

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
    assert sumar(a, b) == esperado #palabra reservada para validar una condición sea verdadera
    
