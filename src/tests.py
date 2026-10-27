from unittest.mock import patch
from app import app
from index import calculator


def test_sum():
    assert calculator().sum(2, 2) == 4


def test_resta():
    assert calculator().resta(5, 3) == 2


def test_multiplicacion_logic():
    assert calculator().multiplicacion(2, 3) == 6


def test_healthz_endpoint():
    client = app.test_client()
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_multiplicacion_toggle_off():
    client = app.test_client()
    with patch("app.is_feature_enabled", return_value=False):
        response = client.get("/multiplicacion?a=4&b=5")
        assert response.status_code == 403
        assert response.json["status"] == "disabled"


def test_multiplicacion_toggle_on():
    client = app.test_client()
    with patch("app.is_feature_enabled", return_value=True):
        response = client.get("/multiplicacion?a=4&b=5")
        assert response.status_code == 200
        assert response.json["result"] == 20
