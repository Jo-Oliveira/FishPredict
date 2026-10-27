import pytest

from src.recomendacao import nota, indice
from src.models import Condicoes
from src.databases import peixes_dic


def test_no_centro_devolve_100():
    assert nota(25, 20, 30) == 100

def test_indice_condicoes_perfeitas_devolve_100():
    robalo = peixes_dic['robalo']
    condicoes = Condicoes(temperatura_agua=16.0, vento=17.5, ondulacao=1.0)
    assert indice(robalo, condicoes) == pytest.approx(100)