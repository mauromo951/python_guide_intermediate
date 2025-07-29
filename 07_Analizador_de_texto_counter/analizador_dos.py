from collections import Counter

def leer_texto(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

def contar_palabras(texto):
    palabras = texto.lower().replace(".", "").split()
    return Counter(palabras)

def contar_letras(texto):
    letras = [c for c in texto.lower() if c.isalpha()]
    return Counter(letras)

def caracteres_unicos(texto):
    return set(texto)

if __name__ == "__main__":
    texto = leer_texto("texto_dos.txt")

    palabras = contar_palabras(texto)
    letras = contar_letras(texto)
    caracteres = caracteres_unicos(texto)

    print("\n--- Análisis de texto ---")
    print("Total de palabras:", sum(palabras.values()))
    print("Top 5 palabras más comunes:", palabras.most_common(5))
    print("Total de letras:", sum(letras.values()))
    print("Top 5 letras más comunes:", letras.most_common(5))
    print("Caracteres únicos:", caracteres)
    print("Cantidad:", len(caracteres))
