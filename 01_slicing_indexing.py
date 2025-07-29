#Slicing
#Extraer un fragmento de una secuencia


numero = "1,2,3,4-4(5,3)5"
print(numero[::2]) 
#Resultado 12344535 va de un número a número, los puntos son para iniciar desde la pisicón 0
#Y va de 2 en 2 posiciones

celular = "(+52) 551876782"
print(celular[6::1])
#Resultado 551876782, empieza desde la posición 6 y va de un en uno
#igual se puede colocar 6::

numeros_voltear = "987654321"
print(numeros_voltear[::-1])#voltea toda la secuencia

#Seleccion la posición de la posición 6 a la 3 y la voltea
print(numeros_voltear[6:3:-1], "Este es la original: ",numeros_voltear) 

