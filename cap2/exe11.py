num = eval(input("num = "))
res = 0

while num != 0:
    dig = num % 10
    res = res * 10
    res = res + dig
    num = num // 10

print(res)
