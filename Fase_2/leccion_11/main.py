from utils.logger import logger, LOG_FILE
from utils.errors import DivisionByZeroError
import os



def dividir():
    a = int(input("Selecciona tu primer número: "))
    b = int(input("Selecciona tu segundo numero: "))
    try:
        if b == 0:
            raise DivisionByZeroError()
        resultado = a / b
        logger.info("Division exitosa: %s / %s = %s", a, b, resultado)
        return print(f"El resultado de la divison es: {resultado}")
     
    except DivisionByZeroError as e:
        logger.error(f"Error de division: {e}")
        return None
    except Exception as e:
        logger.exception("Ocurrio un error inesperado")
        return None
    
def mostrar_logs(n=5):
    if not os.path.exists(LOG_FILE):
        print("⚠️ No hay logs aún.")
        return

    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
        #Se agrega errors, ya que el log tiene acentos
        lineas = f.readlines()
        ultimos = lineas[-n:]
        print("\n=== Últimos Logs ===")
        for linea in ultimos:
            print(linea.strip())
        print("====================")
         
    
def menu():

    while True:

        print("1.Realizar division")
        print("2.Ver logs")
        print("3.Salir")
        opcion = input("Selecciona tu opcion: ")

        if opcion == "1":
            dividir()            
        elif opcion == "2":
            try:
                n_logs = int(input("Selecciona cantidad de logs a ver (1-10): "))
                if n_logs < 1 or n_logs > 10:
                    print("⚠️ Número fuera de rango, se mostrarán 5 logs por defecto.")
                    n_logs = 5
            except ValueError:
                print("⚠️ Entrada inválida, se mostrarán 5 logs por defecto.")
                n_logs = 5

            mostrar_logs(n_logs)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida")
            


if __name__ == "__main__":
    print("=== Demo módulo utils ===")
    """
    # Caso correcto
    print("10 / 2 =", dividir(10, 2))
    
    # Caso división entre cero
    print("10 / 0 =", dividir(10, 0))
    
    # Caso con error inesperado
    print("10 / 'a' =", dividir(10, "a"))
    
    a = int(input("Selecciona tu primer número: "))
    b = int(input("Selecciona tu segundo numero: "))
    print(dividir(a,b))"""
    menu()