def filtra_pares(tuplo):
    res = ()
    for n in tuplo:
        if not isinstance(n, int):
            raise ValueError("filtra_pares: argumento não inteiro")
        elif n % 2 == 0:
            res = res + (n,)

    return res
