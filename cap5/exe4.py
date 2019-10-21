def elemento_matriz(matriz, i, j):
    if i >= len(matriz) or j >= len(matriz[0]):
        raise ValueError("elemento_matriz: i e j invalidos")
    return matriz[i][j]
