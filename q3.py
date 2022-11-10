import math
import sys


def calcula_posiciosamento_cidades(numero_cidades, lista_coordenadas):
    x = 0.0
    y = 0.0

    for i in range(0, len(lista_coordenadas), 2):
        x += lista_coordenadas[i]
        y += lista_coordenadas[i+1]

    x = x / numero_cidades
    y = y / numero_cidades

    raio = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    return x, y, raio


def executa():
    coordenadas = []

    with open("entrada.txt", "r") as arquivo_coordenadas:
        numero_cidades = sys.maxsize

        while numero_cidades:
            numero_cidades = int(arquivo_coordenadas.readline().replace("\n", ""))
            coordenada = []

            for i in range(0, numero_cidades):
                linha = arquivo_coordenadas.readline().replace("\n", "")
                coordenada.append(float(linha.split(" ")[0]))
                coordenada.append(float(linha.split(" ")[1]))

            if coordenada:
                coordenadas.append(coordenada)

    k = 1
    for coordenada in coordenadas:
        x, y, raio = calcula_posiciosamento_cidades(numero_cidades=len(coordenada), lista_coordenadas=coordenada)
        print(f"instancia {k}\n {x} {y} {raio}\n")
        k += 1


if __name__ == "__main__":
    executa()
