#Función ZIP(), convierte en tuplas, union de dos o más iterables, listas, dicts, sets, 
#De diferente tipo de variable

nom_usuario = ["Alex", "Robert", "BOB"]
contrsna = ("123", "abc", "cba")
fecha_creacion = ["hoy", "Mañana", "Pasado"]

usuarios = list(zip(nom_usuario,contrsna,fecha_creacion))

#for i in zip(nom_usuario,contrsna):
#    print(i)

for i,k,j in usuarios:
    print(f"Usuario: {i}, Pass: {k}, Fecha creación: {j}" )


###### Ejemplo de LOGS

logs = (1, 2, 3, 4, "hola")
mensaje_error = ["200", "404", "415", "502", "307"]



log_completo = zip(logs, mensaje_error)

print(type(log_completo))

for i in log_completo:
    print(i)