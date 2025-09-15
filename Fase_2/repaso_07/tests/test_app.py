import pytest
import sqlite3
from database import crear_tabla, agregar_tarea, obtener_tareas, marcar_completada, eliminar_tarea, DB_NAME

@pytest.fixture(autouse=True)
def setup_db():
    # Crear tabla limpia antes de cada test
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS tareas")
    conn.commit()
    conn.close()
    crear_tabla()
    yield

def test_agregar_tarea():
    agregar_tarea("Estudiar Python")
    tareas = obtener_tareas()
    assert len(tareas) == 1
    assert tareas[0][1] == "Estudiar Python"

def test_marcar_completada():
    agregar_tarea("Probar pytest")
    tareas = obtener_tareas()
    marcar_completada(tareas[0][0])
    tareas = obtener_tareas()
    assert tareas[0][2] == 1  # completada = True

def test_eliminar_tarea():
    agregar_tarea("Eliminarme")
    tareas = obtener_tareas()
    eliminar_tarea(tareas[0][0])
    tareas = obtener_tareas()
    assert len(tareas) == 0
