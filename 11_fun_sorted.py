#Función de orden superior

#Sorted es una función integrada que devuelve una 
#nueva lista ordenada a partir de los elementos de un iterable

#Ejemplo

jugador = [("Lebron",23,"Lakers"),("Giannis",34,"Bucks"),("Kd",7,"Suns")]

#Ordenar a partir del número de jugador

lista_jugadores_numero = sorted(jugador,key=lambda x:x[1], reverse=True) #De mayor a menor
lista_jugadores_numero_dos = sorted(jugador,key=lambda x:x[1]) #De menos a manor
print(lista_jugadores_numero)
print(lista_jugadores_numero_dos)

