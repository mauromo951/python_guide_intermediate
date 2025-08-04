#Función de Orden Superior

#reduce(función, iterable)
#Reduce toda una colección a un solo valor aplicando una función acumulativa.

from functools import reduce

numeros = [1,2,3,4,5]

num = reduce(lambda x, y:x+y,numeros)
print(num)
