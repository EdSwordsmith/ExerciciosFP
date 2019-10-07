def explode(num):
    if not isinstance(num, int):
        raise ValueError("explode: argumento não inteiro")

    nums = ()
    while num > 0:
        nums = (num % 10,) + nums
        num = num // 10

    return nums
