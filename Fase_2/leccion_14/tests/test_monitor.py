import pytest
from unittest.mock import patch
from monitor import verificar_servicio

@patch("monitor.requests.get")
def test_verificar_servicio_up(mock_get):
    mock_get.return_value.status_code = 200
    estado, codigo = verificar_servicio("https://example.com")
    assert estado == "UP"
    assert codigo == 200

@patch("monitor.requests.get", side_effect=Exception("Timeout"))
def test_verificar_servicio_down(mock_get):
    estado, codigo = verificar_servicio("https://example.com")
    assert estado == "DOWN"
    assert codigo is None
