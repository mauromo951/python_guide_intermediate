import sys, os, pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.usuarios import Usuario

# --- FIXTURE ---
@pytest.fixture #Funcion fixture, que es reutilizable 
def usuario_dummy():
    """Crea un usuario de prueba que se puede usar en varios tests."""
    return Usuario("Mauro", 25)

# --- TESTS ---
def test_usuario_mayor_de_edad(usuario_dummy):
    #assert usuario_dummy.es_mayor_de_edad() is True
    #assert usuario_dummy.es_mayor_de_edad() is not True
    objeto = Usuario("",(16 + 2))
    assert objeto.es_mayor_de_edad() is not False
    

def test_usuario_menor_de_edad():
    u = Usuario("Carlos", 15)
    assert u.es_mayor_de_edad() is False

def test_edad_negativa():
    """Aquí probamos pytest.raises para errores."""
    with pytest.raises(ValueError, match="edad no puede ser negativa"):
        Usuario("Error", -5)

"""
##NOTAS##
Fixture (usuario_dummy) → genera datos de prueba una sola vez y los comparte. 
Test normal (assert) → verificamos resultados esperados. 
pytest.raises → validamos que una función lance el error correcto.
"""