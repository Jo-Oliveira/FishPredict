from src.models import Condicoes, Peixe


def nota(valor: float, minimo: float, maximo: float) -> float:
    """Calcula a nota do peixe.
    Lógica: atribuir um mínimo e máximo (0 a 100),
    onde 100 é no centro do intervalo ideal.
    Para depois sabermos calcular a distância em que o valor está de cada um
    desses extremos.

    Args:
        valor: valor medido (por exemplo, a temperatura da água em °C).
        minimo: limite inferior do intervalo ideal.
        maximo: limite superior do intervalo ideal.

    Returns:
        Nota entre 0 e 100.
    """

    if minimo == maximo and valor == minimo:
        return 100
    if minimo == maximo and valor != minimo:
        return 0
    centro = minimo + (maximo - minimo) / 2

    distancia = abs(valor - centro)

    raio = maximo - centro

    return max(0.0, ( 1- distancia / raio) * 100)

def nota_temperatura(peixe, condicoes):
    """Calcula a nota da temperatura.
    Vai buscar as condições ideias da temperatura do peixe e
    compara com as do momento atual.
    """
    minimo, maximo = peixe.temperatura_da_agua
    return nota(condicoes.temperatura_agua, minimo, maximo)

def nota_vento(peixe, condicoes):
    """Calcula a nota do vento.
    Vai buscar as condições ideais de vento do peixe e
    compara com as do momento atual.
    """
    minimo, maximo = peixe.condicoes_vento_ideais
    return nota(condicoes.vento, minimo, maximo)

def nota_ondulacao(peixe, condicoes):
    """Calcula a nota da ondulação.
    Vai buscar as condições ideais de ondulação do peixe e
    compara com as do momento atual.
    """
    minimo, maximo = peixe.condicoes_ondulacao_ideal
    return nota(condicoes.ondulacao, minimo, maximo)

def indice(peixe: Peixe, condicoes: Condicoes) -> float:
    """Calcula o índice do peixe.
    É a média ponderada das notas de temperatura, vento e ondulação (0 a 100).
    """
    nota_t = nota_temperatura(peixe, condicoes) * peixe.pesos["temperatura"]
    nota_v = nota_vento(peixe, condicoes) * peixe.pesos['vento']
    nota_o = nota_ondulacao(peixe, condicoes) * peixe.pesos["ondulacao"]

    return nota_t + nota_v + nota_o
