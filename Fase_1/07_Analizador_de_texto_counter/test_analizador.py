from collections import Counter


def test_contar_palabras():
    texto = "Python es genial. Python es poderoso."
    palabras = texto.lower().replace(".", "").split()
    c = Counter(palabras)
    assert c["python"] == 2
    assert c["es"] == 2
    assert c["genial"] == 1
    assert c["poderoso"] == 1

def test_contar_letras():
    texto = "Python es poderoso"
    solo_letras = [c for c in texto.lower() if c.isalpha()]
    c = Counter(solo_letras)
    assert c["o"] == 4
    assert c["p"] == 1
    assert c["y"] == 2

def test_caracteres_unicos():
    texto = "ABBA\n"
    caracteres = set(texto)
    assert len(caracteres) == 3  # 'A', 'B', '\n'
    assert "\n" in caracteres
    assert "A" in caracteres or "a" in caracteres
