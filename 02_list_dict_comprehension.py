#Sirve para escribir codigo más compacto, para manipular logs, JSONs, datos filtrados.

#List comprehension
#[expresión for elemento in iterable if condición]

numeros = [1, 2, 3, 4, 5, 10]
pares_cuadrados = [n**2 for n in numeros if n % 2 == 0]
print(pares_cuadrados) 


#Crea lista de rango 90 0-89
lista_dos = [i * 2 for i in range(11) if i % 2 == 0]
print(lista_dos)

def sum_five(number):
    return number + 5

lista_tres = [sum_five(i) for i in range(10)]
print(lista_tres)

cuadrados = [i**2 for i in numeros]
print(cuadrados)


# Dict comprehension
# dict = {clave:valor}
#{clave: valor for clave, valor in iterable if condición}

valores = {"a": 40, "b": 80, "c": 60}
filtrados = {k: v for k, v in valores.items() if v > 50}
print(filtrados)

valor = {i : i**2 for i in range(0,11,2) }
print(valor)


# Set comprehension, set no permite duplicados y no hay orden garantizado
# set = {valor}

lista_set = [5,2,3,3,3,2,4,1,55,20]

#cuadrados_set = {222}

cuadrados_set = {x**2 for x in lista_set}
print(cuadrados_set,lista_set)