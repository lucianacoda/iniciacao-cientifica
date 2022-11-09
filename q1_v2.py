def verifica_vizinho_linha(matriz, novo_i, j, n, vizinhos):
    if 0 <= novo_i < n:
        vizinhos.append(matriz[novo_i][j])
    return vizinhos


def verifica_vizinho_coluna(matriz, novo_j, i, m, vizinhos):
    if 0 <= novo_j < m:
        vizinhos.append(matriz[i][novo_j])
    return vizinhos


def calcula_media_vizinhos(matriz, n, m, i, j):
    vizinhos = []
    vizinhos = verifica_vizinho_linha(matriz=matriz, novo_i=i - 1, j=j, n=n, vizinhos=vizinhos)
    vizinhos = verifica_vizinho_linha(matriz=matriz, novo_i=i + 1, j=j, n=n, vizinhos=vizinhos)
    vizinhos = verifica_vizinho_coluna(matriz=matriz, novo_j=j - 1, i=i, m=m, vizinhos=vizinhos)
    vizinhos = verifica_vizinho_coluna(matriz=matriz, novo_j=j + 1, i=i, m=m, vizinhos=vizinhos)

    media = 0.0
    for vizinho in vizinhos:
        #print(vizinho)
        media += vizinho  # media = media + vizinho

    media = media / len(vizinhos)
    return media


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    n = 2
    m = 2
    i = 0
    j = 1
    ref = A[i][j]
    media_vizinhos = calcula_media_vizinhos(matriz=A, n=n, m=m, i=i, j=j)

    print(f"A média aritmetica dos vizinhos de {ref} é {media_vizinhos}")
