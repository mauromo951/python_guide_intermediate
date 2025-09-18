class SaldoInsuficienteError(Exception): #Excpecion personalizada
    pass
class Depositoceroynegativo(Exception): #Excpecion personalizada
    pass

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente en la cuenta")
            #Uso de excpecion personalizada
        self.saldo -= monto
        return self.saldo
    def depositar(self, monto):
        if monto <= 0:
            raise Depositoceroynegativo("Deposito inválido")
            #Uso de excpecion personalizada
        self.saldo += monto
        return self.saldo
    
cuenta = CuentaBancaria(1000)
"""
try:
    cuenta.retirar(150)
except SaldoInsuficienteError as e:
    print(f"Error: {e}")
"""
def menu():
    print("1.Realizar retiro")
    print("2.Realizar deposito")
    print("3.Consultar saldo")
    print("4.Salir")

def run():

    while True:
        menu()
        opcion = input("Elije una opcion: ")

        if opcion == "1":
            cantidad = int(input("Selecciona la cantidad a retirar: "))
            try:
                cuenta.retirar(cantidad)
                
            except SaldoInsuficienteError as e:
                print(f"Error: {e}")
                #menu()
                return False
        if opcion == "2":
            cantidad = int(input("Selecciona la cantidad a retirar: "))
            try:
                cuenta.depositar(cantidad)
            except ValueError:
                print("Error: El valor introducido no es un número válido.")
                print("Por favor, vuelve a introducir los valores.")
            except Depositoceroynegativo as e:
                print(f"Error: {e}")

            
        if opcion == "3":
            print(f"Tu saldo es: {cuenta.saldo}")
        if opcion == "4":
            break

if __name__ == "__main__":
    run()