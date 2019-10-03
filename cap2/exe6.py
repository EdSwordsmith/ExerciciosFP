a = eval(input("Escreva o primeiro numero, a = "))
b = eval(input("Escreva o segundo numero, b = "))
c = eval(input("Escreva o terceiro numero, c = "))

if a >= b and a >= c:
    print("O primeiro numero e o maior")
elif b >= a and b >= c:
    print("O segundo numero e o maior")
elif c >= a and c >= b:
    print("O terceiro numero e o maior")
