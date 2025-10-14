import sqlite3
import logging
from pathlib import Path

# --- Configuración del directorio de logs ---
base_dir = Path(__file__).resolve().parent.parent  # sube a la raíz del proyecto
log_dir = base_dir / "leccion_13/logs"
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "app.log"

# --- Configurar logging ---
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
)

# --- Excepciones personalizadas ---
class AppError(Exception):
    """Excepción base."""
    pass

class UsuarioDuplicadoError(AppError):
    """Error cuando se intenta registrar un usuario ya existente."""
    pass

class UsuarioNoEncontradoError(AppError):
    """Error cuando se intenta borrar un usuario que no existe."""
    pass

# --- Funciones de base de datos ---
def conectar_db():
    """Conecta o crea la base de datos local."""
    db_path = base_dir / "leccion_13/usuarios.db"
    return sqlite3.connect(db_path)

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            edad INTEGER NOT NULL
        )
    """)
    conn.commit()
    logging.info("Tabla 'usuarios' verificada o creada.")

def insertar_usuario(conn, nombre, edad):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad)) #? uso de placeholders, para evitar sql inyection
        conn.commit()
        logging.info(f"✅ Usuario agregado: {nombre}, {edad} años")
        print(f"Usuario '{nombre}' agregado correctamente.")
    except sqlite3.IntegrityError:
        logging.error(f"❌ Error: usuario duplicado '{nombre}'")
        raise UsuarioDuplicadoError(f"El usuario '{nombre}' ya existe.")

def obtener_usuarios(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, edad FROM usuarios")
    return cursor.fetchall()

def eliminar_usuario(conn, nombre, edad):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE nombre = ? AND edad = ?", (nombre, edad))
    conn.commit()

    if cursor.rowcount == 0:
        # cursor.rowcount indica cuántas filas se afectaron por la sentencia SQL.
        #Si es 0, significa que no había coincidencias.
        logging.warning(f"⚠️ Intento de borrar usuario no encontrado: {nombre}, {edad} años")
        raise UsuarioNoEncontradoError(f"El usuario '{nombre}' con edad {edad} no existe.")
    else:
        logging.info(f"🗑️ Usuario eliminado: {nombre}, {edad} años")
        print(f"✅ Usuario '{nombre}' eliminado correctamente.")
        