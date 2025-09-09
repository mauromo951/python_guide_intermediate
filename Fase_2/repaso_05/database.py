import sqlite3

DB_NAME = "usuarios.db"

def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            ciudad TEXT
        )
    """)
    conn.commit()
    conn.close()


def insertar_usuario(id, nombre, email, ciudad):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO usuarios (id, nombre, email, ciudad)
        VALUES (?, ?, ?, ?)
    """, (id, nombre, email, ciudad))
    conn.commit()
    conn.close()


def obtener_usuarios():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, email, ciudad FROM usuarios")
    resultados = cursor.fetchall()
    conn.close()
    return resultados
