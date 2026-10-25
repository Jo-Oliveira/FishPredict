from src.models import Peixe, Condicoes
def nota(valor, minimo, maximo):
    centro = minimo + (maximo - minimo) / 2

    distancia = abs(valor - centro)

    raio = maximo - centro

    return max(0, ( 1- distancia / raio) * 100)

print(nota(28, 20, 30))

def nota_temperatura(peixe, condicoes):
    minimo, maximo = peixe.temperatura_da_agua
    return nota(condicoes.temperatura_agua, minimo, maximo)