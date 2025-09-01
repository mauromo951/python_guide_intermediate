#Repaso OOP, encapsulamiento, herencia, polimorfismo, herencia múltiple y composición
"""
Encapsulamiento → Controlar el acceso a los atributos/métodos.

Herencia → Reutilizar código de una clase base en clases hijas.

Polimorfismo → Usar el mismo método pero con diferentes comportamientos según la clase.

Herencia múltiple → Una clase hereda de varias.

Composición → Una clase contiene objetos de otra, en lugar de heredar.
"""

##Ejemplo
# Clase base
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    # Método polimórfico
    def mover(self):
        return "El vehículo se está moviendo 🚗"


# Herencia: diferentes tipos de vehículos
class Auto(Vehiculo):
    def mover(self):
        return f"El auto {self.marca} avanza por la carretera 🚙"


class Bicicleta(Vehiculo):
    def mover(self):
        return f"La bicicleta {self.marca} pedalea en el carril 🚴"


class ScooterElectrico(Vehiculo):
    def mover(self):
        return f"El scooter {self.marca} se desliza en la ciudad 🛴"


# Composición: un auto con motor y batería
class Motor:
    def encender(self):
        return "Motor encendido ✅"


class Bateria:
    def nivel(self):
        return "Batería al 90% ⚡"


class AutoElectrico(Auto):
    def __init__(self, marca):
        super().__init__(marca)
        self.motor = Motor()
        self.bateria = Bateria()

    def mover(self):
        return f"El auto eléctrico {self.marca} circula en modo silencioso 🔋"


# -------------------------
# Uso de polimorfismo
if __name__ == "__main__":
    vehiculos = [
        Auto("Toyota"),
        Bicicleta("Trek"),
        ScooterElectrico("Xiaomi"),
        AutoElectrico("Tesla")
    ]

    for v in vehiculos:
        print(v.mover())  # Cada objeto responde de forma distinta aunque se llame igual

