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
    return codifica(codifica(codifica(texto)))
