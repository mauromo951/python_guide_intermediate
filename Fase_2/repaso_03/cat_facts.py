import requests
import json
from datetime import datetime
import os

ARCHIVO = "cat_facts.json"

def obtener_facts():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # devuelve un dict con la info
    else:
        print("⚠️ Error al consultar la API")
        return None

def guardar_fact(fact):
    datos = []

    # Si el archivo ya existe, cargamos lo anterior
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)

    # Añadimos timestamp
    fact["timestamp"] = datetime.now().isoformat()

    datos.append(fact)

    # Guardamos con indentación
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    fact = obtener_facts()
    if fact:
        guardar_fact(fact)
        print("✅ Fact guardado en", ARCHIVO)
