#Consulta del clima

import requests
import json
import logging

# Configurar logging básico
logging.basicConfig(filename="Fase_2/leccion_12/api_errors.log", level=logging.ERROR, encoding="utf-8")

def obtener_ubicacion_actual():
    """
    Obtiene la ubicación actual (latitud, longitud y ciudad)
    usando la IP pública del usuario.
    """
    try:
        response = requests.get("http://ip-api.com/json", timeout=5)
        response.raise_for_status()

        data = response.json()
        ciudad = data#data.get("city")
        lat = data.get("lat")
        lon = data.get("lon")

        if not ciudad or not lat or not lon:
            raise ValueError("No se pudo obtener la ubicación actual.")

        return ciudad, lat, lon

    except requests.RequestException as e:
        logging.error(f"Error al obtener ubicación: {e}")
        print("⚠️ No se pudo obtener tu ubicación actual.")
        return None, None, None
    
def obtener_clima_por_coordenada():
    try:
        lat = float(input("Ingresa primer coordenada (latitud): "))
        lon = float(input("Ingresa segunda coordenada (longitud): "))
        return lat,lon
    except requests.RequestException as e:
        logging.error(f"Error al obtener ubicación: {e}")
        print("⚠️ No se pudo obtener tu ubicación actual.")
        return  None, None



def obtener_clima(ciudad: str = None, lat: float = None, lon: float = None):
    """
    Consulta el clima de una ciudad o por coordenadas.
    """
    try:
        if ciudad and not (lat and lon):
            coordenadas = {
                "CDMX": (19.4326, -99.1332),
                "Monterrey": (25.6866, -100.3161),
                "Guadalajara": (20.6597, -103.3496)
            }

            if ciudad not in coordenadas:
                raise ValueError("Ciudad no válida o no disponible en el sistema.")
            lat, lon = coordenadas[ciudad]

        if not lat or not lon:
            raise ValueError("No se recibieron coordenadas válidas.")

        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        return data["current_weather"]["temperature"]

    except Exception as e:
        logging.error(f"Error al obtener clima: {e}")
        print("❌ Error al consultar el clima.")
        return None

    except requests.Timeout:
        logging.error("⏰ Timeout: la API tardó demasiado en responder.")
        print("Error: el servidor no respondió a tiempo.")
    except requests.RequestException as e:
        logging.error(f"⚠️ Error de conexión o HTTP: {e}")
        print("Error: no se pudo conectar con la API.")
    except (json.JSONDecodeError, KeyError):
        logging.error("📄 Error: respuesta JSON inválida o faltan datos.")
        print("Error: los datos recibidos no son válidos.")
    except ValueError as e:
        logging.error(f"❌ {e}")
        print(e)
    except Exception as e:
        logging.error(f"🚨 Error inesperado: {e}")
        print("Ocurrió un error inesperado.")
