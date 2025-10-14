from db_utils import (
    conectar_db,
    crear_tabla,
    insertar_usuario,
    eliminar_usuario,
    obtener_usuarios,
    UsuarioDuplicadoError,
    UsuarioNoEncontradoError,
)
from pathlib import Path

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar usuario")
    print("2. Listar usuarios")
    print("3. Ver últimos logs")
    print("4. Eliminar usuario")
    print("5. Salir")

def mostrar_logs(n=5):
    log_path = Path(__file__).resolve().parent.parent / "logs" / "app.log"
    if not log_path.exists():
        print("No hay logs registrados aún.")
        return
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        lineas = f.readlines()[-n:]
    print("\n--- Últimos logs ---")
    for linea in lineas:
        print(linea.strip())

def run():
    conn = conectar_db()
    crear_tabla(conn)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            edad = input("Edad: ").strip()
            try:
                insertar_usuario(conn, nombre, int(edad))
            except UsuarioDuplicadoError as e:
                print("⚠️", e)
            except ValueError:
                print("⚠️ Edad inválida. Debe ser un número.")
        elif opcion == "2":
            usuarios = obtener_usuarios(conn)
            if usuarios:
                print("\nUsuarios registrados:")
                for nombre, edad in usuarios:
                    print(f"👤 {nombre} ({edad} años)")
            else:
                print("No hay usuarios registrados.")
        elif opcion == "4":
            nombre = input("Nombre del usuario a eliminar: ").strip()
            edad_input = input("Edad: ").strip()

            try:
                edad = int(edad_input)
                confirmacion = input(f"⚠️ ¿Seguro que deseas eliminar a '{nombre}' ({edad} años)? (s/n): ").lower()

                if confirmacion == "s":
                    eliminar_usuario(conn, nombre, edad)
                else:
                    print("❎ Operación cancelada. El usuario no fue eliminado.")

            except UsuarioNoEncontradoError as e:
                print("⚠️", e)
            except ValueError:
                print("⚠️ Edad inválida.")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    run()
