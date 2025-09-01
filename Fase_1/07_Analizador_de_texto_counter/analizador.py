"""
Objetivo: Construir un script que lea un texto y muestre:

1.Total de palabras, palabras más comunes

2.Total de letras, letras más comunes

3.Letras más comunes

4.Palabras más comunes

5.Caracteres únicos
"""
#Abrir TXT
with open("texto.txt", 'r') as t:
    texto = t.read()

from collections import Counter

#1
palabras = texto.lower().split()
contar_palabras = Counter(palabras)
print("Total de palabras: ", len(palabras) )
#4
print("Estas son las palabras más comunes: ", contar_palabras)

#2
letras = [c for c in texto.lower() if c.isalpha()]
conteo_letras = Counter(letras)
print("Total de letras: ", len(letras))
#3
print("Letras más comunes: ", conteo_letras.most_common(5))

unicos = set(texto)
print("Caractéres unicos: ", unicos)
print("Cantidad: ", len(unicos))
