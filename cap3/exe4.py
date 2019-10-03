from cap3.exe3 import area_circulo


def area_coroa(r1, r2):
    if r1 > r2:
        raise ValueError("r1 não pode ser maior que r2")

    return area_circulo(r2) - area_circulo(r1)


print(area_coroa(4, 6))
