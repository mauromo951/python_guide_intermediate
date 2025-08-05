#Metodos, self y atirbutos
#self es una palabra clave obligatoria en los métodos de una clase en Python.
#Representa al propio objeto (la instancia que se está creando o usando).
#Con self, el objeto se puede dar acceso a sus propios atributos y métodos.

class Carro():
    #Especificaciones de un carro
    total_ruedas= 4 # Atributo de clase
    def __init__(self, marca, modelo): #Lo que está en los parentesis son atributos
        self.marca = marca
        self.modelo = modelo
        self.combustible = "Gasolina"

    def acelerar(self): #Método
        """Simula que el carro avanza"""
        print(self.marca.title() + " avanza")
        
    def frenar(self):
        """Simula que el carro ha frenado"""
        print(self.marca.title() + " ha frenado")

mi_carro = Carro("Porsche", 2025)

print("Mi carro es un: " + mi_carro.marca.title())
print("Mi carro es modelo: "+ str(mi_carro.modelo)) 

mi_carro.acelerar()
mi_carro.frenar()


otro_carro = Carro("Suburban", 2024)

print("Mi carro es una: " + otro_carro.marca.title())
print("Mi carro es modelo: "+ str(otro_carro.modelo)) 
print(f"La combustión de mi carro es: {otro_carro.combustible}")
print(f"Mi carro tiene {otro_carro.total_ruedas} ruedas")
print(f"Mi carro tiene {Carro.total_ruedas} ruedas")

otro_carro.frenar()
otro_carro.acelerar()

##Otro ejemplo
class Persona:
    especie = "Humano"  # Atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def cumplir_edad(self):
        self.edad += 1 #a += b → es lo mismo que a = a + b, para este caso self.edad = self.edad + 1
        print(f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años.")

# Crear objetos
p1 = Persona("Mauro", 28)
p2 = Persona("Lucía", 25)

# Usar métodos
p1.saludar()          # Hola, soy Mauro y tengo 28 años.
p1.cumplir_edad()    # ¡Feliz cumpleaños Mauro! Ahora tienes 29 años.

# Atributo de clase
print(p1.especie)     # Humano
print(p2.especie)     # Humano
