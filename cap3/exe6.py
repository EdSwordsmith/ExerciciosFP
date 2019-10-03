from cap3.exe5 import bissexto

meses31 = ('jan', 'mar', 'mai', 'jul', 'ago', 'out', 'dez')
meses30 = ('abr', 'jun', 'set', 'nov')


def dia_mes(mes, ano):
    if mes in meses31:
        return 31
    elif mes in meses30:
        return 30
    elif mes == 'fev' and bissexto(ano):
        return 29
    elif mes == 'fev' and not bissexto(ano):
        return 28
    else:
        raise ValueError("Mes não existe")
