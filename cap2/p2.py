num = eval(input("Escreva um numero "))
res = 0
pot = 1

while num != 0:
    dig = num % 10

    if dig == 8: # condicao simplificada
        dig = 0
    elif dig % 2 == 0:
        dig = dig + 2
    elif dig == 1: # condicao simplificada
        dig = 9
    else:
        dig = dig - 2

    res = res + dig * pot
    pot = pot * 10
    num = num // 10

print(res)
