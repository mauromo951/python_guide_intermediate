#Encapsulamiento
#Significa ocultar los detalles internos de un objeto y exponer solo lo necesario a través de métodos y propiedades controladas.
# self._atributo cuando se utiliza "_" no debe de accederse a ese atributo o es privado
"""
Nivel	    Ejemplo	        Acceso desde fuera	        Uso común
Público	    self.valor	    Libre	                    Datos y métodos abiertos
Protegido	_self.valor	    Libre (convención)	        Interno pero accesible con cuidado
Privado	    __self.valor	Difícil (name mangling)	    Ocultar detalles críticos
"""


class Jugador:

    tipo = "Basquetbolista"

    def __init__(self, nombre, equipo, numero, posicion, altura, puntos):
        self.nombre = nombre
        self._equipo = equipo
        self.numero = numero
        self._posicion = posicion
        self.__altura = altura
        self._puntos = puntos

    #get acceder a un atributo
    def get_numero(self):
        return self.numero
    #set para modificar valor de un atributo
    def set_numero(self,numero):
        if numero < 100 and numero > -1 :
            self.numero = numero
        else:
            print("El numero no puede ser mayor de 99 y menor que 0")
            print(f"El numero '{numero}' no pudo ser modificado")

    #Decorador
    @property
    def equipo(self):
        return self._equipo

    @equipo.setter
    def equipo(self,equipo):            
        if equipo == str(equipo): #Forzar a que sea un string
            self._equipo = equipo
        else:
            print("Digita un string valido") 

    def encestar_doble(self):
        print(f"El jugador {self.nombre} ha anotado {self._puntos+2} ")

    
jugador_1 = Jugador("KD", "Rockets", 7 , "F", 2.11, 500)
print(f"El jugador {jugador_1.nombre}, tiene {jugador_1._puntos} puntos")

jugador_1._puntos = 600
print(f"El jugador {jugador_1.nombre}, tiene {jugador_1._puntos} puntos")

#jugador_1.__altura = 2.01
#print(f"El jugador {jugador_1.nombre}, mide:'{jugador_1.__altura} ' ")

#print(jugador_1.get_posicion())

#jugador_1.set_numero(-11)
jugador_1.set_numero(0)
print(f"El número de {jugador_1.nombre} es: '{jugador_1.get_numero()}'")

team = jugador_1.equipo
print(f"El equipo de {jugador_1.nombre} es {team}")

#Modificar equipi
jugador_1.equipo = "Lakers"
print(f"El equipo de {jugador_1.nombre} es {jugador_1.equipo}")


##Otro ejemplo

class Servidor:
    def __init__(self, ip, puerto):
        self.ip = ip                # Público
        self._puerto = puerto       # Protegido
        self.__clave_admin = "root123"  # Privado

    def conectar(self):
        print(f"Conectando a {self.ip}:{self._puerto}")

    def __reset_admin(self):
        print("Clave de administrador reiniciada")

    def solicitar_reset(self, clave):
        if clave == self.__clave_admin:
            self.__reset_admin()
        else:
            print("Clave incorrecta")

srv = Servidor("192.168.0.10", 8080)
srv.conectar()                  
print(srv.ip)                   
print(srv._puerto)              
# print(srv.__clave_admin)      # Error
srv.solicitar_reset("root122")  
