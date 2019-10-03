def valor(q, j, n):
    if n < 0 or q < 0 or j < 0 or j > 1:
        raise ValueError("Argumentos Inválidos")
    return q * (1 + j) ** n


def duplicar(q, j):
    n = 1
    while valor(q, j, n) < 2 * q:
        n = n + 1
    return n
