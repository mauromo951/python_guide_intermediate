from collections import Counter
from analizador_dos import contar_palabras, contar_letras, caracteres_unicos

def test_contar_palabras():
    texto = "Python es genial. Python es poderoso."
    c = contar_palabras(texto)
    assert c["python"] == 2
    assert c["es"] == 2
    assert c["genial"] == 1
    assert c["poderoso"] == 1

def test_contar_letras():
    texto = "Python es poderoso"
    c = contar_letras(texto)
    assert c["o"] == 3
    assert c["p"] == 1
    assert c["y"] == 1
    assert c["s"] == 2

def test_caracteres_unicos():
    texto = "ABBA\n"
    chars = caracteres_unicos(texto)
    assert len(chars) == 3
    assert "\n" in chars
    assert "A" in chars or "a" in chars
