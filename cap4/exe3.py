def implode(tuplo):
    num = 0
    for d in tuplo:
        if not isinstance(d, int):
            raise ValueError("implode: elemento não inteiro")
        else:
            num = num * 10 + d

    return num


def implode_while(tuplo):
    i = 0
    num = 0
    while i < len(tuplo):
        if not isinstance(tuplo[i], int):
            raise ValueError("implode: elemento não inteiro")
        else:
            num = num * 10 + tuplo[i]
        i = i + 1

    return num
