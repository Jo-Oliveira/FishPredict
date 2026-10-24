def nota(valor, minimo, maximo):
    centro = minimo + (maximo - minimo) / 2

    distancia = abs(valor - centro)

    raio = maximo - centro

    return max(0, ( 1- distancia / raio) * 100)

print(nota(28, 20, 30))