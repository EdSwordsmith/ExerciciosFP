num = eval(input("num = "))
res = 0
pot = 1

while num > 0:
    dig = num % 10
    if dig % 2 == 1:
        res = res + dig * pot
        pot = pot * 10
    num = num // 10

print(res)
