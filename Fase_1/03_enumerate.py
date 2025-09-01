#enumarate()

lista_nombres = ["Hola1", "Hola2", "Hola3"]
lista_dos = ["Jpala"]

for indice in range(3):
    print(indice, lista_nombres[indice], "#####")

for i, valor in enumerate(lista_nombres): #enumarate (0(indice), valor)
    print(i,valor)
#enumarate, para este for jala el Hola1 y lo guarda en valor. 
# Y lo va enumerando inicia en 0 y lo guarda en i conforme va avanzando

logs = ["200", "OK", "ERROR - DB","22", "ERROR-TIMEOUT" ]

for i, valor in enumerate(logs):
    if "ERROR" in valor:
        print(f"Error en linea {i}: {valor}")

#Para este caso, enumera los logs. La númeración se guarda en i, el mensaje del log en valor
#Si hay ERROR en algun log, lo detecta y muestra en que línea y su error



