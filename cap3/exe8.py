from math import sqrt


def primo(n):
    i = 2
    p = True
    while i <= sqrt(n):
        if n % i == 0:
            p = False
            break
        i = i + 1
    return p and n != 1
