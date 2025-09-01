#Funcion de Orden Superior, High Order Superior
# Map(), map(función, iterable)

#Toma la funcion declarada y la aplica a una secuencia o un iterable
#Ejemplo

lista_nombres = ['jorge', 'leo', 'domi']

lista_mayus = map(str.upper, lista_nombres)

print(tuple(lista_mayus))


lista_frutas = ["uva","melon","fresa"]
sufix = '_fruta'

def add_sufix(fruta):
    return fruta+sufix

lista_fruta_sufix = list(map(add_sufix,lista_frutas))
print(lista_fruta_sufix)

#Mismo caso otra representación usando lambda

lista_fruta_sufix_dos = list(map(lambda x:x+sufix,lista_frutas))
print(lista_fruta_sufix_dos)

#Otro ejemplo

numeros = [1, 2, 3, 4]

# Elevar al cuadrado
cuadrados = list(map(lambda x: x**2, numeros))
otro_caso = list(map(lambda x:x+x, numeros ))

print(cuadrados)  # [1, 4, 9, 16]
print(otro_caso)
