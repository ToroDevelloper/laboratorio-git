from app import app
from index import calculator


def test_sum():
    assert calculator().sum(2, 2) == 4


def test_resta():
    assert calculator().resta(5, 3) == 2


def test_multiplicacion():
    assert calculator().multiplicacion(2, 3) == 6


def test_healthz_endpoint():
    client = app.test_client()
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
