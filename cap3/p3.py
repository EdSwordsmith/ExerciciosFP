def eh_triangular(num):
    if not isinstance(num, int) or num <= 0:
        raise ValueError('eh_triangular: o argumento nao e inteiro positivo')

    n = 0
    i = 1
    while n < num:
        n = n + i
        i = i + 1

    return n == num
