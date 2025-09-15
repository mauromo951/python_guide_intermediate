import sqlite3

DB_NAME = "tareas.db"

def crear_tabla():
    """
    Crea la tabla de tareas si no existe.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            completada INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def agregar_tarea(titulo):
    """
    Inserta una nueva tarea.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tareas (titulo) VALUES (?)", (titulo,))
    conn.commit()
    conn.close()

def obtener_tareas():
    """
    Devuelve todas las tareas como lista de tuplas.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, completada FROM tareas")
    tareas = cursor.fetchall()
    conn.close()
    return tareas

def marcar_completada(id):
    """
    Marca una tarea como completada.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tareas SET completada = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def eliminar_tarea(id):
    """
    Elimina una tarea por ID.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
