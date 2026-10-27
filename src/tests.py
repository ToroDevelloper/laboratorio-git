from index import calculator
def test_sum():
    assert calculator().sum(2, 2) == 4
def test_resta():
    assert calculator().resta(5, 3) == 2
def test_multiplicacion():
    # Fallo intencional para demostrar la red de seguridad del CI
    assert calculator().multiplicacion(2, 3) == 999