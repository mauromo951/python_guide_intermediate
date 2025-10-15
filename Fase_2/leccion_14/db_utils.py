import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "monitor.db"

def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_db():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            estado TEXT NOT NULL,
            codigo INTEGER,
            timestamp TIMESTAMP CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def guardar_resultado(url, estado, codigo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO servicios (url, estado, codigo) VALUES (?, ?, ?)",
        (url, estado, codigo)
    )
    conn.commit()
    conn.close()

def obtener_historial(limit=10):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servicios ORDER BY id DESC LIMIT ?", (limit,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados
