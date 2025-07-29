#reversed() Funcion, crea una iteración que voltea los valores, pero la lista original se conserva

errores = ["Paso 1", "ERROR A", "Paso 2", "ERROR B"]
resultado = list()
for paso in reversed(errores):
    resultado.append(paso)
    #.append(valor) agrega todo el objeto como una sola unidad, sin dividirlo.
    
print(resultado)


#reverse() Metodo, modifica el iterable y voltea los valores

lista_errores = ["200 OK", "404 Not found", "503 Forbidden"]
print(f"Logs antes del reverse:{lista_errores}")
lista_errores.reverse()
print(lista_errores)