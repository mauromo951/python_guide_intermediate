#mocks
#Se usa para simular funciones externas (APIs, DB, archivos) y no depender de ellas en los tests.

#sirve para crear objetos simulados que reemplazan componentes reales durante las pruebas,
# permitiendo probar la lógica de una unidad de código de forma aislada

#Ejemplo 1
"""
import requests
from unittest.mock import patch

def obtener_clima(ciudad):
    resp = requests.get(f"https://api.weatherapi.com/{ciudad}")
    return resp.json()["temp"]



def test_obtener_clima():
    fake_response = {"temp": 26}

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = fake_response

        
        temp = obtener_clima("ACOLMAN")
        #return temp

        assert temp == 26
        mock_get.assert_called_once()  # Verifica que sí se llamó a la API

print(test_obtener_clima())
"""

#Ejemplo 2

import requests
from unittest.mock import patch


def obtener_clima(ciudad: str) -> int:
    """Devuelve la temperatura de la ciudad"""
    url = f"https://api.ejemplo.com/clima?ciudad={ciudad}"
    resp = requests.get(url)
    data = resp.json()
    return data["temp"]


#Usando mock
def test_obtener_clima_mock():
    fake_response = {"temp": 25}

    # Simulamos la llamada a requests.get
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = fake_response

        temp = obtener_clima("CDMX")

        assert temp == 25
        mock_get.assert_called_once()

#Sin usar mock
def test_obtener_clima_real():
    temp = obtener_clima("CDMX")
    assert isinstance(temp, int)  # Solo validamos que devuelva un número