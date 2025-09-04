
from db import cargar_tareas, guardar_tareas
from tareas import Tarea

def mostrar_menu():
    print("\n1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")

def run():
    tareas = [Tarea(**t) for t in cargar_tareas()]

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ")
            tareas.append(Tarea(titulo))
            print("✅ Tarea agregada.")

        elif opcion == "2":
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")

        elif opcion == "3":
            indice = int(input("Número de tarea: ")) - 1
            if 0 <= indice < len(tareas):
                tareas[indice].marcar_completada()
                print("✅ Tarea completada.")
            else:
                print("⚠️ Número inválido.")

        elif opcion == "4":
            guardar_tareas([t.__dict__ for t in tareas])
            print("💾 Tareas guardadas. Saliendo...")
            break

        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    run()