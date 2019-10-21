def remove_multiplos(lista, n):
    res = []
    for e in lista:
        if e % n != 0:
            res.append(e)
    return res
