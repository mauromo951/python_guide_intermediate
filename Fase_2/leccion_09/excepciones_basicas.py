#Excepciones básicas

#Ejemplo 1
"""
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre 0.")
        return None

print(dividir(10, 2))  # ✅ 5.0
print(dividir(10, 0))  # ⚠️ No se puede dividir entre 0.
"""
#Ejemplo 2

while True:
    try:
        numerador = float(input("Introduce el numerador: "))
        denominador = float(input("Introduce el denominador: "))
        cociente = numerador / denominador
        print(f"{cociente}")
        break
    except ValueError:
        print("Error: El valor introducido no es un número válido.")
        print("Por favor, vuelve a introducir los valores.")
    
#else y finally
def abrir_archivo(nombre):
    try:
        f = open(nombre, "r")
    except FileNotFoundError:
        print("⚠️ Archivo no encontrado.")
    else:
        print("✅ Archivo abierto con éxito.")
        f.close()
    finally:
        print("🔒 Fin del intento de abrir archivo.")

abrir_archivo("existe.txt")
abrir_archivo("no_existe.txt")
