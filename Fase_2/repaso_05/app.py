"""
Objetivo

1. Consultar datos desde una API pública.

2. Guardarlos en una base SQLite.

3. Mostrar resultados desde la base.
"""

import requests
from database import crear_tabla, insertar_usuario, obtener_usuarios

API_URL = "https://jsonplaceholder.typicode.com/users"

def consultar_api():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def main():
    # Crear tabla
    crear_tabla()

    # Consultar API
    usuarios = consultar_api()
    print(f"Se obtuvieron {len(usuarios)} usuarios de la API.")

    # Guardar en DB
    for u in usuarios:
        insertar_usuario(
            id=u["id"],
            nombre=u["name"],
            email=u["email"],
            ciudad=u["address"]["city"]
        )

    # Mostrar resultados
    print("\nUsuarios en la base de datos:")
    for usuario in obtener_usuarios():
        print(usuario[0:4], len(usuario))


if __name__ == "__main__":
    main()
