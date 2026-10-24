from src.recomendacao import nota

def test_no_centro_devolve_100():
    assert nota(25, 20, 30) == 100