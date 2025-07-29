#Funciones como objetos

"""
En Python, las funciones son objetos de primera clase. Eso significa que:
-Se pueden asignar a variables.
-Se pueden pasar como argumentos a otras funciones.
-Se pueden retornar desde funciones.
-Se pueden almacenar en estructuras como listas o diccionarios.
"""

def saludar():
    return "¡Hola!"

def ejecutar_funcion(func):
    resultado = func()  # Ejecuta la función recibida
    print(resultado)

ejecutar_funcion(saludar)

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def operar(func, x, y):
    return func(x, y)

print(operar(sumar, 10, 5))  # Resultado: 15
print(operar(restar, 10, 5))  # Resultado: 5
