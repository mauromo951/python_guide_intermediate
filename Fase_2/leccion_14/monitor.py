import requests
from logger import registrar_evento
from db_utils import guardar_resultado

def verificar_servicio(url, timeout=3):
    try:
        respuesta = requests.get(url, timeout=timeout)
        estado = "UP" if respuesta.status_code == 200 else "DOWN"
        guardar_resultado(url, estado, respuesta.status_code)
        registrar_evento(f"{url} → {estado} ({respuesta.status_code})")
        return estado, respuesta.status_code

    except requests.exceptions.RequestException as e:
        guardar_resultado(url, "DOWN", None)
        registrar_evento(f"{url} → DOWN (Error: {e})", nivel="error")
        return "DOWN", None
