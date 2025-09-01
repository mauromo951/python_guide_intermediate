"""
Objetivo del Proyecto:
Crear funciones que:
-Eliminen valores vacíos o None
-Recorten espacios
-Corrijan mayúsculas/minúsculas
-Conviertan tipos cuando sea posible
"""

datos = ["  juan", None, "Ana  ", "", "pedro", "LUIS", "    ", "carla", 123, None, "MARÍA", '']

def limpiar_valor(valor):
    if isinstance(valor, str):
        valor = valor.strip()  # Quitar espacios
        if valor == "":
            return None
        return valor.lower()  # Convertir a minúsculas
    return None  # Si no es string o es None

def limpiar_lista(lista):
    return [limpiar_valor(valor) for valor in lista if limpiar_valor(valor) is not None]

lista_limpia = limpiar_lista(datos)
print(lista_limpia)
# ['juan', 'ana', 'pedro', 'luis', 'carla', 'maría']

def contar_unicos(lista):
    return {valor: lista.count(valor) for valor in set(lista)}
print(contar_unicos(lista_limpia))
print(contar_unicos(datos))

######### Ejemplo completo
# ---------------------- Funciones de limpieza ----------------------

def limpiar_valor(valor):
    if isinstance(valor, str):
        valor = valor.strip()
        if valor == "":
            return None
        return valor.lower()
    return None

def limpiar_lista(lista):
    return [limpiar_valor(v) for v in lista if limpiar_valor(v) is not None]

def contar_unicos(lista):
    return {v: lista.count(v) for v in set(lista)}

# ---------------------- Interfaz simple por consola ----------------------

def mostrar_menu():
    print("\n--- Mini sistema de limpieza de datos ---")
    print("1. Ver datos originales")
    print("2. Limpiar texto")
    print("3. Contar valores únicos")
    print("4. Salir")

def ejecutar_sistema():
    datos = ["  juan", None, "Ana  ", "", "pedro", "LUIS", "    ", "carla", 123, None, "MARÍA"]
    datos_limpios = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(f"Datos originales: {datos}")

        elif opcion == "2":
            datos_limpios = limpiar_lista(datos)
            print(f"Datos limpios: {datos_limpios}")

        elif opcion == "3":
            if not datos_limpios:
                print("Primero debes limpiar los datos (opción 2).")
            else:
                print("Conteo de valores únicos:")
                for k, v in contar_unicos(datos_limpios).items():
                    print(f"{k}: {v}")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

# ---------------------- Ejecutar ----------------------

if __name__ == "__main__":
    ejecutar_sistema()
