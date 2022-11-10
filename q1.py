def calcula_media_vizinhos(matriz, n, m, i, j):
    vizinhos = []
    if i - 1 >= 0:
        vizinhos.append(matriz[i - 1][j])
    if i + 1 < n:
        vizinhos.append(matriz[i + 1][j])
    if j - 1 >= 0:
        vizinhos.append(matriz[i][j - 1])
    if j + 1 < m:
        vizinhos.append(matriz[i][j + 1])

    media = 0.0
    for vizinho in vizinhos:
        # print(vizinho)
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
