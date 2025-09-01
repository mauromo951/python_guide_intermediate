#Diccionarios anidados, dict con dict
#Funciona para manejo de datos y acceder a datos
paises = {"Mexico":{"name":"MX","code":52, "is_ame":True},
            "USA":{"name":"EUA","code":1, "is_ame":False},
            "Brasil":{"name":"BRA", "code":22, "Ciudades": ["Sao Paulo","Rio de Janeiro"]}}

print(paises.get("Mexico").get("code")) #52

codigo_mx = paises ["Mexico"]["code"]
print(codigo_mx)

#Acceder a las ciudades de Brasil
bra_cities = paises["Brasil"]["Ciudades"]
print(bra_cities,type(bra_cities)) #Lo imprime como lista
for i in bra_cities:
    print (i,type(i)) #Lo imprime como string


#Acceder a todos los codes de los paises

for name, valor in paises.items():
    print(name,valor["code"])


#Comprobar si Brasil tiene una ciuidad "Buenos Aires"
if paises["Brasil"]["Ciudades"] == "Buenos Aires":
    print("Brasil tiene como ciudad buenos aires")
else:
    print("Buenos Aires no es de Brasil")

#Acceso seguro a datos por medio de get()
#Ejemplo de dato JSON
data = {
    "usuario": {
        "nombre": "Mauro",
        "config": {
            "notificaciones": True,
            "tema": "oscuro"
        }
    }
}

tema = data.get("usuario", {}).get("config", {}).get("tema", "claro")
print(tema)  # 'oscuro' o 'claro' si faltan claves

#SETDEAFULT(), no cambia valores de una clave, solo crea nuevas

config = data.setdefault("usuario", {}).setdefault("config", {})
config.setdefault("idioma", "español")
print(data["usuario"]["config"]["idioma"])  # 'español'
print(data["usuario"])

#Ejemplo para SRE


status_db = data.get("services", {}).get("db", {}).get("status", "ok")
print("Estado de la base de datos:", status_db)



def validar(): 
    if paises["Brasil"]["Ciudades"] == "Buenos Aires":
        return True
    else:
        return False
print(validar())