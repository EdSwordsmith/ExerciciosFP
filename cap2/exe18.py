num = eval(input("num = "))
maior_zeros = 0
zeros = 0

while num != 0:
    if num % 10 == 0:
        zeros = zeros + 1
    else:
        if zeros > maior_zeros:
            maior_zeros = zeros
        zeros = 0
    num = num // 10

print(maior_zeros)
