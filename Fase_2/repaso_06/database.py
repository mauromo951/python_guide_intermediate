import sqlite3

DB_NAME = "usuarios.db"

def crear_tabla():
    """
    Crea la tabla 'usuarios' en la base de datos SQLite si no existe.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            email TEXT,
            ciudad TEXT
        )
    """)
    conn.commit()
    conn.close()

def insertar_usuario(id, nombre, email, ciudad):
    """
    Inserta un usuario en la base de datos.
    
    Args:
        id (int): ID único del usuario.
        nombre (str): Nombre completo del usuario.
        email (str): Correo electrónico.
        ciudad (str): Ciudad de residencia.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO usuarios VALUES (?, ?, ?, ?)", (id, nombre, email, ciudad))
    conn.commit()
    conn.close()

def obtener_usuarios():
    """
    Obtiene todos los usuarios almacenados en la base de datos.
    
    Returns:
        list[tuple]: Lista de tuplas con los usuarios (id, nombre, email, ciudad).
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios
