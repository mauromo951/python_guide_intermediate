from database import crear_tabla, agregar_tarea, obtener_tareas, marcar_completada, eliminar_tarea

def mostrar_menu():
    print("\n1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def run():
    crear_tabla()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ")
            agregar_tarea(titulo)
            print("✅ Tarea agregada.")

        elif opcion == "2":
            tareas = obtener_tareas()
            if not tareas:
                print("⚠️ No hay tareas.")
            for t in tareas:
                estado = "✅" if t[2] else "❌"
                print(f"{t[0]}. {t[1]} [{estado}]")

        elif opcion == "3":
            id_tarea = int(input("ID de la tarea a completar: "))
            marcar_completada(id_tarea)
            print("👌 Tarea completada.")

        elif opcion == "4":
            id_tarea = int(input("ID de la tarea a eliminar: "))
            eliminar_tarea(id_tarea)
            print("🗑️ Tarea eliminada.")

        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    run()
