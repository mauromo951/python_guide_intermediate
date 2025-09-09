class Usuario:
    def __init__(self, nombre, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa") #raise manda una excepción
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        return self.edad >= 18
