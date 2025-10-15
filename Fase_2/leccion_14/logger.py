import logging
from pathlib import Path

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "monitor.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

def registrar_evento(mensaje, nivel="info"):
    if nivel == "error":
        logging.error(mensaje)
    else:
        logging.info(mensaje)
