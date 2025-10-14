import sqlite3
import pytest
from db_utils import crear_tabla, insertar_usuario, obtener_usuarios, UsuarioDuplicadoError

@pytest.fixture
def conexion_temporal():
    # Base en memoria (no persiste)
    conn = sqlite3.connect(":memory:")
    crear_tabla(conn)
    yield conn
    conn.close()


def test_insertar_y_obtener(conexion_temporal):
    conn = conexion_temporal

    insertar_usuario(conn, "Mauro", 27)
    insertar_usuario(conn, "Ana", 30)

    usuarios = obtener_usuarios(conn)

    assert len(usuarios) == 2
    assert usuarios[0][0] == "Mauro"
    assert usuarios[1][1] == 30


def test_usuario_duplicado(conexion_temporal):
    conn = conexion_temporal

    insertar_usuario(conn, "Mauro", 27)
    with pytest.raises(UsuarioDuplicadoError):
        insertar_usuario(conn, "Mauro", 40)
