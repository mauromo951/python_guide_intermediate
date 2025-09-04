from app.tareas import Tarea

def test_crear_tarea():
    tarea = Tarea("Estudiar Python")
    assert tarea.titulo == "Estudiar Python"
    assert tarea.completada == False

def test_marcar_completada():
    tarea = Tarea("Hacer ejercicio")
    tarea.marcar_completada()
    assert tarea.completada == True
