def soma_cumulativa(lista):
    res = []
    soma = 0
    for n in lista:
        soma += n
        res.append(soma)
    return res
