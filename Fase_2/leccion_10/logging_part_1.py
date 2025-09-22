"""
import logging

# Configuración básica
logging.basicConfig(level=logging.DEBUG)

logging.debug("Este es un mensaje de depuración")
logging.info("Inicio del programa")
logging.warning("Esto es una advertencia")
logging.error("Ha ocurrido un error")
logging.critical("Error crítico")
"""

#Ejemplo

import logging
import os

# 1. Carpeta donde está el archivo actual
base_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Construir la ruta del log en esa carpeta
log_path = os.path.join(base_dir, "usuario.log")

logging.basicConfig(
    
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def login(usuario, contraseña):
    if usuario == "admin" and contraseña == "1234":
        logging.info(f"Usuario {usuario} inició sesión con éxito.")
        return True
    else:
        logging.warning(f"Intento fallido de login con usuario: {usuario}")
        return False

# Simulación
login("admin", "1234")
login("mauro", "wrongpass")

resultado_log = "2025-09-22 16:43:17,600 - INFO - Usuario admin inicio sesion con exito."
resultado_log_dos= "2025-09-22 16:43:17,600 - WARNING - Intento fallido de login con usuario: mauro"
print("Se generó el archivo usuarios.log")
print(f"{resultado_log},\n{resultado_log_dos}" )