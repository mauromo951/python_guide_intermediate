#Herencia

class Jugador: #Clase padre

    def __init__(self, nombre, deporte, altura):
        self.nombre = nombre
        self.__deporte = deporte
        self.__altura = altura
    
    #Decoradores
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        if 0 < altura < 2.99:
            self.__altura = altura
        else:
            print("No se puede definir la altura")

    


class Basquebolista(Jugador): #Clase hijo

    def __init__(self, nombre, deporte, altura, position, balon):
        super().__init__(nombre, deporte, altura) #acceder a atributos o metodos de la clase padre
        self.position = position
        self.balon = balon

class Futbolista(Jugador):
    def __init__(self, nombre, deporte, altura, equipo):
        super().__init__(nombre, deporte, altura)
        self.equipo = equipo


jugador_1 = Basquebolista("Lebron", "Basquetbol", 2.06, "FW", "Molten")
print(f"El jugador se llama {jugador_1.nombre}, y su poisicion es {jugador_1.position} y su altura es {jugador_1.altura}")

jugador_2 = Futbolista("Messi", "Futbol",1.70,"Barcelona")
jugador_2.altura = 3.0
print(f"EL jugador {jugador_2.nombre} juega en el equipo {jugador_2.equipo} y su altura es: {jugador_2.altura}")




        

