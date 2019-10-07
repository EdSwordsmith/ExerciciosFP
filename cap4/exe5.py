from cap4.exe2 import explode
from cap4.exe3 import implode
from cap4.exe4 import filtra_pares


def algarismos_pares(num):
    if not isinstance(num, int):
        raise ValueError("algarismos_pares: num nao inteiro")
    return implode(filtra_pares(explode(num)))
