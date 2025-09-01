#Funciones lambda

#Primera representación comun

def retornar_nota(estudiante):
    return estudiante[1]

lista_estudiante = [('Pedro', 4.2), ('Pepe',5.7), ('Maria', 4.2), ('Carlos',9.7)]

lista_ordenada = sorted(lista_estudiante, key=retornar_nota, reverse=True)
print(lista_ordenada)


lambda estudiante: estudiante[1]
#Uso practico lamba x:x[1]

#Aquí ya no tiene porque decalarar y llamar a la función, se declara directo en el key

lista_ordenada = sorted(lista_estudiante, key=lambda x:x[1])
print(lista_ordenada)

#Otro Ejemplo

lista_ejemplo = [1,2,3]
retorno = lambda x:x[1]

print(retorno(lista_ejemplo))

#Ejemplo de suma
valor1 = 2
valor2 = 3
suma = lambda x,y :valor1 + valor2

print(suma(valor1,valor2))

#Otra forma de representarlo más compacto

suma_dos = lambda x, y : x + y
print(suma_dos(4,3))

