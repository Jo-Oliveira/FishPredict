import copy

import pytest

from src.databases import peixes_dic
from src.models import Condicoes, Peixe
from src.recomendacao import indice, nota


def criar_peixe(pesos: dict[str, float]) -> Peixe:
    """Cria um robalo com os pesos inseridos pelo utilizador."""
    return Peixe(
        nome="Robalo",
        nome_cientifico="Dicentrarchus labrax",
        habitat="Rebentação / Zonas de rocha e areia",
        tecnica="Spinning",
        amostra_ideal="Amostra rija / Vinil",
        tamanho_minimo_cm=36,
        epoca_pesca=[9, 10, 11, 12, 1, 2, 3],
        melhor_hora_dia=[(6, 9), (18, 21)],
        condicoes_vento_ideais=(10.0, 25.0),
        fase_mare_ideal="vazante",
        condicoes_ondulacao_ideal=(0.5, 1.5),
        tipo_agua="Mar aberto / Estuário",
        profundidade_ideal=3.0,
        temperatura_da_agua=(12.0, 20.0),
        fase_lunar="cheia ou nova",
        pesos= pesos,
    )


def test_no_centro_devolve_100():
    assert nota(25, 20, 30) == 100

def test_indice_condicoes_perfeitas_devolve_100():
    robalo = peixes_dic['robalo']
    condicoes = Condicoes(temperatura_agua=16.0, vento=17.5, ondulacao=1.0)
    assert indice(robalo, condicoes) == pytest.approx(100)

def test_nota_intervalo_de_um_so_valor_nao_rebenta():
    assert nota(25, 25, 25) == 100

def test_peso_maior_na_ondulacao_baixa_mais_o_indice():
    robalo = peixes_dic['robalo']

    peixe_a = copy.deepcopy(robalo)
    peixe_a.pesos = {"temperatura": 0.3, "vento": 0.2, "ondulacao": 0.5}

    peixe_b = copy.deepcopy(robalo)
    peixe_b.pesos = {"temperatura": 0.45, "vento": 0.45, "ondulacao": 0.1}

    condicoes = Condicoes(temperatura_agua=16.0, vento=17.5, ondulacao=0.0)
    assert indice(peixe_a, condicoes) < indice(peixe_b, condicoes)

def test_pesos_que_nao_somam_1():
    with pytest.raises(ValueError):
        criar_peixe(pesos={"temperatura": 0.5, "vento": 0.5, "ondulacao": 0.5})

def test_pesos_validos():
    peixe = criar_peixe({"temperatura": 0.25, "vento": 0.30, "ondulacao": 0.45})
    assert peixe.nome == "Robalo"