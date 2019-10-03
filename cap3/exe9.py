from cap3.exe8 import primo


def n_esimo_primo(n):
    i = 0
    num = 1
    while i < n:
        num = num + 1
        if primo(num):
            i = i + 1
    return num
