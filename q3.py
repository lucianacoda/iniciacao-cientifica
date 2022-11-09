import math


def calcula_posiciosamento_cidades(numero_cidades, lista_coordenadas):
    x = 0.0
    y = 0.0
    for coordenada in lista_coordenadas:  # [[x0, y0], [x1, y1], ..., [xn, yn] onde n = numero_cidades-1 ]
        x += coordenada[0]
        y += coordenada[1]

    x = x / numero_cidades
    y = y / numero_cidades

    raio = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    return raio
