def misterio(num):
    n = num
    primeiro = 0
    ultimo = 0
    i = 0
    inv = 0

    while n > 0:
        ultimo = n % 10
        if i == 0:
            primeiro = ultimo
        inv = inv * 10 + ultimo
        i = i + 1
        n = n // 10

    if i != 3 or abs(primeiro - ultimo) <= 1:
        return "Condições não verificadas"

    ns = abs(num - inv)
    nsi = 0
    n = ns

    while n > 0:
        d = n % 10
        nsi = nsi * 10 + d
        n = n // 10

    return ns + nsi
