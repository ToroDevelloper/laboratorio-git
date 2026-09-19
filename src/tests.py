from index import calculator

def test_sum():
    assert calculator().sum(2, 2) == 4

def test_resta():
    assert calculator().resta(5, 3) == 2
