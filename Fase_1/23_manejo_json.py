#JSON
"""
Función	                Uso
json.dump()	        Guarda datos en un archivo JSON
json.dumps()	    Convierte datos a un string JSON
json.load()	        Lee datos desde un archivo JSON
json.loads()	    Convierte un string JSON a objeto Python
"""

import json

json_str = '{"nombre":"Mauro","edad":28,"pais":"Mexico"}'
print(json_str)

python_dict = json.loads(json_str) #Transformar en un diccionario
print(type(python_dict))
print(python_dict['edad'])

data = {"jugador":"Messi", 
        "equipo":"barcelona", 
        "numero":10,
        "campeonatos":["UCL", "La_liga", "Mundial", "Copa_rey"]}

json_data = json.dumps(data) #Lo convierte a string
print(type(json_data))

print(json_data[7:3:-1])

json_data = json.dumps(data,indent=4,separators=(",",":"), sort_keys=True )
print(json_data)


#Clase, con atributos y métodos
class Jugador:
    profesion = "Futbolista"
    

    def __init__(self,nombre,numero,sueldo): # Constructor
        self.nombre = nombre
        self.numero = numero
        self.sueldo = sueldo

jugador_1 = Jugador("Neymar", 10, 5000)
print(jugador_1)
json_object_data = json.dumps(jugador_1.__dict__)
print(json_object_data)

## Ultimo ejemplo

class Jugador:
    def __init__(self, nombre, equipo, altura):
        self.nombre = nombre
        self.equipo = equipo
        self.altura = altura

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "equipo": self.equipo,
            "altura": self.altura
        }

# Crear jugador
j1 = Jugador("KD", "Rockets", 2.11)

# Guardar en JSON
with open("jugador.json", "w") as archivo: #Crea el archivo json
    json.dump(j1.to_dict(), archivo, indent=4)

# Leer desde JSON
with open("jugador.json", "r") as archivo:
    datos_jugador = json.load(archivo)

print(datos_jugador)
