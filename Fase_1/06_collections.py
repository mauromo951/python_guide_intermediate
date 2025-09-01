#Collections: Counter, namedtuple, defaultdict, deque, OrderedDict

#Counter
#Crea un diccionarios, realizando un conteo de cuantas veces un valor se repite
from collections import Counter

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter) #Counter({'a': 5, 'b': 4, 'c': 3})
print(type(my_counter.items())) #<class 'dict_items'> dict_items[str, int]
print(my_counter.items())
print(my_counter.keys())
print(my_counter.most_common(1)) #El más comun(1), los dos más comunes (2)

#accede a los 2 más comunes, al segundo miembro y el segundo valor
# [('a', 5), ('b', 4)] -> [('b', 4)] -> 4
print(my_counter.most_common(2)[1][1])
print(list(my_counter.elements()))

"""
Ejemplo
"""
errores = ["500", "404", "200", "500", "200", "500"]
conteo = Counter(errores)

print(conteo)  # Counter({'500': 3, '200': 2, '404': 1})
print(conteo["500"])  # 3

#namedtuple
#Tuplas con nombres en lugar de índices. Muy útil para registros, config, respuestas estructuradas.
#Crea una clase
from collections import namedtuple

point = namedtuple('point', ['x','y','j'])

pt = point(11, 22, 23) #Se asgina valores a x, y
print(pt, pt.index(23)) #Que pocision tiene el valor, en la tupla en este caso 2

"""
Ejemplo
"""
Usuario = namedtuple("Usuario", ["nombre", "rol"])
mauro = Usuario("Mauro", "SRE")

print(f"Nombre: {mauro.nombre}")  # Mauro
print(f"Rol: {mauro.rol}")     # SRE

#OrderedDict
#se utiliza para mantener el orden en que se insertan los elementos en un diccionario
from collections import OrderedDict

ordered = OrderedDict()
ordered['b'] = 2
ordered['z'] = 4
ordered['a'] = 1
print(ordered)

#defaultdict
#facilita el manejo de claves inexistentes, 
#asignando automáticamente un valor predeterminado cuando se intenta acceder a ellas
from collections import defaultdict

usuarios = defaultdict(list) #Inicializa una lista en [] o un int = 0
usuarios["admin"].append("Mauro")
usuarios["admin"].append("Lucía")
usuarios["dev"].append("Carlos")

print(usuarios, usuarios["admin"])

#deque
#permite agregar y eliminar elementos por ambos extremos
from collections import deque

ejemplo = deque()

ejemplo.append(1)
ejemplo.append('Hola')
ejemplo.appendleft("Se agregó a la izquierda")
#ejemplo.pop()#remueve el último dato
#ejemplo.clear()# remueve todo
ejemplo.extend([4,5,6]) #se agrega como lista, ya que extend solo permite un dato, no 3 ints
#ejemplo.extendleft('Agrega más a la izquierda') #Lo agrega volteado a,d,r,e,i,u, letra por letra
ejemplo.rotate(2) #rota dos a la izquierda
ejemplo.rotate(-1) #rota el valor inicial a la derecha
print(type(ejemplo), ejemplo)

