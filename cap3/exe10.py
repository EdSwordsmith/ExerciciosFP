from math import floor


def dia_da_semana(q, m, ano):
    k = ano % 100
    m, k = mes_ano(m, k)
    j = floor(ano / 100)
    h = (q + floor(13 * (m + 1) / 5) + k + floor(k / 4) + floor(j / 4) - 2 * j) % 7
    return nome_dia(h)


def mes_ano(m, ano):
    if m < 3:
        m = m + 12
        ano = ano - 1
    return m, ano


def nome_dia(h):
    if h == 0:
        return 'sabado'
    elif h == 1:
        return 'domingo'
    elif h == 2:
        return 'segunda'
    elif h == 3:
        return 'terça'
    elif h == 4:
        return 'quarta'
    elif h == 5:
        return 'quinta'
    else:
        return 'sexta'
