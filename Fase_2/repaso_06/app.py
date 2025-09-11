import requests
from database import crear_tabla, insertar_usuario, obtener_usuarios

API_URL = "https://jsonplaceholder.typicode.com/users"

def consultar_api():
    """
    Consulta la API pública y devuelve la lista de usuarios en formato JSON.
    
    Returns:
        list[dict]: Lista de usuarios con campos como id, name, email, address.
    Raises:
        requests.exceptions.RequestException: Si ocurre un error en la petición.
    """
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()

def main():
    """
    Flujo principal de la aplicación:
    1. Crea la tabla en SQLite.
    2. Descarga usuarios de la API.
    3. Inserta los usuarios en la base de datos.
    4. Muestra todos los usuarios almacenados.
    """
    crear_tabla()
    usuarios = consultar_api()
    print(f"Se obtuvieron {len(usuarios)} usuarios de la API.")

    for u in usuarios:
        insertar_usuario(u["id"], u["name"], u["email"], u["address"]["city"])

    print("\nUsuarios en la base de datos:")
    for usuario in obtener_usuarios():
        print(usuario)

if __name__ == "__main__":
    main()
