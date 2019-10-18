def codifica(texto):
    par = ""
    impar = ""

    for i in range(len(texto)):
        if i % 2 == 0:
            par = par + texto[i]
        else:
            impar = impar + texto[i]

    return par + impar


def descodifica(texto):
    par = texto[:round(len(texto)/2)]
    impar = texto[round(len(texto)/2):]
    res = ""

    for i in range(len(impar)):
        res = res + par[i] + impar[i]
    if len(par) != len(impar):
        res = res + par[-1]

    return res

