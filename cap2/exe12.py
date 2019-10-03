x = eval(input("x = "))
n = eval(input("n = "))

soma = 0
numerador = 1
denominador = 1
i = 0

while i <= n:
    num = numerador / denominador
    soma = soma + num

    i = i + 1
    numerador = numerador * x
    denominador = denominador * i

print(soma)
