#Mensajes de error personalizados.
#Verificar si hay errores
#finally ejecutar siempre incluso con errores.

try:
    x=int(input("Ingresa un num: "))
    y=int(input("Ingresa un num: "))
    resultado= x/y
    print(resultado)

except ZeroDivisionError:
    print("No se puede dividir entre 0, intenta con otro número")

except ValueError:
    print("Ingresa solo num enteros.")

finally:
    print("Fin de programa")
#else:
#    print("Resultado :",resultado)


#Otro ejemplo de errores personalizados
class ErrorEdadInvalida(Exception):
    """Error lanzado cuando la edad no es válida."""
    pass

def registrar_usuario(edad):
    if edad < 0 or edad > 120:
        raise ErrorEdadInvalida(f"Edad inválida: {edad}")
    print(f"Usuario registrado con edad: {edad}")

try:
    registrar_usuario(120)
except ErrorEdadInvalida as e:
    print(f"ERROR: {e}")

