import math
from dataclasses import dataclass


class Peixe:
    def __init__(self, nome: str, nome_cientifico: str, habitat: str, tecnica: str, amostra_ideal: str, tamanho_minimo_cm: float,
                 epoca_pesca: list[int], melhor_hora_dia: list[tuple[int, int]], condicoes_vento_ideais: tuple[float, float],
                 fase_mare_ideal: str, condicoes_ondulacao_ideal: tuple[float, float],tipo_agua: str, profundidade_ideal: float,
                 temperatura_da_agua: tuple[float, float], fase_lunar: str, pesos: dict[str, float]):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.habitat = habitat
        self.tecnica = tecnica
        self.amostra_ideal = amostra_ideal
        self.tamanho_minimo_cm = tamanho_minimo_cm
        self.epoca_pesca = epoca_pesca
        self.melhor_hora_dia = melhor_hora_dia
        self.fase_mare_ideal = fase_mare_ideal
        self.condicoes_vento_ideais = condicoes_vento_ideais
        self.condicoes_ondulacao_ideal = condicoes_ondulacao_ideal
        self.tipo_agua = tipo_agua
        self.profundidade_ideal = profundidade_ideal
        self.temperatura_da_agua = temperatura_da_agua
        self.fase_lunar = fase_lunar
        self.pesos = pesos

        if not math.isclose(sum(pesos.values()), 1.0):
            raise ValueError("A soma dos pesos tem que dar 1")
class LocalPesca:
    def __init__(self, nome: str, latitude: float, longitude: float, tipo_de_agua: str, peixes_comuns: list[Peixe]):
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.tipo_de_agua = tipo_de_agua
        self.peixes_comuns = peixes_comuns

@dataclass
class Condicoes:
    temperatura_agua: float
    vento: float
    ondulacao: float


