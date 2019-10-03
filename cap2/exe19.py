quantia = eval(input("quantia = "))

notas50 = quantia // 50
quantia = quantia % 50

notas20 = quantia // 20
quantia = quantia % 20

notas10 = quantia // 10
quantia = quantia % 10

notas5 = quantia // 5
quantia = quantia % 5

moedas2 = quantia // 2
quantia = quantia % 2

moedas1 = quantia // 1
quantia = quantia % 1

moedas50c = quantia // 0.5
quantia = quantia % 0.5

moedas20c = quantia // 0.2
quantia = quantia % 0.2

moedas10c = quantia // 0.1
quantia = quantia % 0.1

moedas5c = quantia // 0.05
quantia = quantia % 0.05

moedas2c = quantia // 0.02
quantia = quantia % 0.02

moedas1c = quantia // 0.01
quantia = quantia % 0.01

print(notas50, notas20, notas10, notas5)
print(moedas2, moedas1)
print(moedas50c, moedas20c, moedas10c, moedas5c, moedas2c, moedas1c)
