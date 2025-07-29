# logger.py
log_eventos = []

def registrar_evento(*mensajes, **info):
    evento = {
        "mensajes": list(mensajes),
        "info": info
    }
    log_eventos.append(evento)
    return evento

def obtener_log():
    return log_eventos

if __name__ == "__main__":
    registrar_evento("Inicio del sistema", usuario="admin")
    registrar_evento("Fallo en módulo X", usuario="dev", nivel="warning")
    for e in obtener_log():
        print(e)