#Try, except, finally, else

#Ejemplo Try, excep

print("OPCIONES")
print("[1] Suscribirme")
print("[2] Darle like")
print("[3] Deja tu comentario")

print()

#Inicializar variables
opcion = 0
intentos = 0

#bucle hasta que se introduzca una  opción correcta
while opcion < 1 or opcion > 3:
    opcion = input("Selecciona una opcion: ")
    try:
        opcion = int(opcion)
    except ValueError:
        print("Ingresa un número entero")
        opcion = 0
    intentos += 1
    if intentos >= 5:
        print("Has agotado el número de intentos")
        break
else:
    print(f"Has escogido la opcion {opcion}")

#try, except
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("División por cero")
else:
    print("Todo salió bien:", resultado)

#finally
try:
    archivo = open("datos.txt")
except FileNotFoundError:
    print("Archivo no encontrado.")
finally:
    print("Fin del intento de abrir archivo.")

#raise
def verificar_edad(edad):
    if edad < 18:
        raise ValueError("Debes ser mayor de edad.")
    return True

