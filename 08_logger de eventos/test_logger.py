# test_logger.py
from logger import registrar_evento, obtener_log

def test_registro_simple():
    evento = registrar_evento("Error de conexión", usuario="Mauro", nivel="ERROR")
    assert "Error de conexión" in evento["mensajes"]
    assert evento["info"]["usuario"] == "Mauro"

def test_varios_mensajes():
    evento = registrar_evento("Paso 1", "Paso 2", sistema="Red", estado="falló")
    assert len(evento["mensajes"]) == 2
    assert evento["info"]["estado"] == "falló"

def test_log_global():
    log = obtener_log()
    assert len(log) >= 2  # Ya hemos agregado 2 eventos en los tests anteriores
