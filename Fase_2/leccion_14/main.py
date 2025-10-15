from db_utils import inicializar_db, obtener_historial
from monitor import verificar_servicio

def mostrar_menu():
    print("\n1. Verificar servicio")
    print("2. Ver historial")
    print("3. Salir")

def run():
    inicializar_db()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            url = input("Ingresa la URL a verificar: ")
            verificar_servicio(url)

        elif opcion == "2":
            n = int(input("¿Cuántos registros mostrar? "))
            for r in obtener_historial(n):
                print(f"[{r['timestamp']}] {r['url']} → {r['estado']} ({r['codigo']})")

        elif opcion == "3":
            print("👋 Saliendo...")
            break
        else:
            print("⚠️  Opción inválida.")

if __name__ == "__main__":
    run()
