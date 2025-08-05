#Clases y objetos

#Clase, con atributos y métodos
class Jugador:
    profesion = "Futbolista"
    

    def __init__(self,nombre,numero,sueldo): # Constructor
        self.nombre = nombre
        self.numero = numero
        self.sueldo = sueldo



#Objeto
jugador_1 = Jugador("Neymar", 10, 5000)
jugador_2 = Jugador("Messi", 10, 500000)

print(jugador_1.profesion,jugador_1.nombre,jugador_1.numero,jugador_1.sueldo)
print(jugador_2.profesion,jugador_2.nombre,jugador_2.numero,jugador_2.sueldo)

#Para este caso, el atributo profesion sirve para ambos objetos
#Y al crear los métodos, 

########## Otro ejemplo

class Persona:
    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Mauro", 30)
persona2 = Persona("Luis", 25)

persona1.saludar()
persona2.saludar()

def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
