from cap4.exe2 import explode


def num_para_seq_cod(num):
    if not isinstance(num, int) or num <= 0:
        raise ValueError("num_para_seq_cod: valor nao e um inteiro positivo")

    t = explode(num)
    res = ()

    for e in t:
        if e % 2 == 0:
            res = res + ((e + 2) % 10,)
        else:
            res = res + ((e - 2) % 10,)

    return res
