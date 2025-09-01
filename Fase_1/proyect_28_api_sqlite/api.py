## Lógica para consumir API

import requests

def get_pokemon(nombre: str) -> dict:
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
