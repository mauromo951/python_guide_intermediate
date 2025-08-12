#Manejo de archivos leer y escribir TXT
"""
file = open('archivo.txt', 'r')
print(file)
lineas= file.readlines()
print(lineas)
file.close() #Cerrar el documento
"""
## Ejemplo dos
"""
with open('archivo_2.txt','r') as archivo_2:
    lineas_dos = archivo_2.readlines()
    print(lineas_dos)

print(lineas_dos)

for l in lineas_dos:
    print(l.replace('\n',''))
"""

#Ejemplo tres
"""
with open('archivo_2.txt', 'r') as ejemplo_dos:
    conteido = ejemplo_dos.read()
    lineas_dos = conteido.split('\n')
    print(lineas_dos)
"""

#Ejemplo cuatro, al leer saber cuantos caracteres tiene. sin leer está desde la posición 0
"""
with open('archivo_2.txt','r') as archivo_2:
    conteido = archivo_2.read()
    lineas_dos = conteido.split('\n')
    position = archivo_2.tell()
    print(position)
    print(f"El archivo tiene {position} daracteres de Longitud".format(position))
"""

#Ejemplo cinco
"""
with open('archivo_2.txt','r') as archivo_2:
    archivo_2.seek(10) #Inicializar la lectura del archivo en un caracter en específico.
    pos = archivo_2.tell()
    print(pos)
"""

#Ejemplo cinco
"""
with open('archivo_2.txt','r') as archivo_2:
    siguientes_cuatro = archivo_2.read(7) #Leer 7 caracteres
    print(siguientes_cuatro)
"""
"""
#Leer como texto
with open('archivo_2.txt','r') as archivo_2:
    print(type(archivo_2.read()))
#Leer como bytes
with open('archivo_2.txt','rb') as archivo_2:
    print(type(archivo_2.read()))
"""

"""Escitura"""
"""
with open('archivo_3.txt','a') as archivo_2: #'w' borra todo y escribe nuevamente 'a' agrega al archivo
    archivo_2.write('Estas\nescribiendo agregando,,,')
"""

#Ejemplo declarando la codificación

# Abrir en modo lectura
with open("archivo_3.txt", "r", encoding="utf-8") as archivo: #with → cierra el archivo automáticamente al finalizar.

    contenido = archivo.read()
    print(contenido)

#Ejemplo para SRE leer errores en un log

with open("server.log", "r", encoding="utf-8") as log:
    for linea in log:
        if "ERROR" in linea:
            print(linea.strip())
