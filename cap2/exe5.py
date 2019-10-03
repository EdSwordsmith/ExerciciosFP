from math import sqrt

n1 = eval(input("n1 = "))
n2 = eval(input("n2 = "))
n3 = eval(input("n3 = "))
n4 = eval(input("n4 = "))
n5 = eval(input("n5 = "))

media = (n1 + n2 + n3 + n4 + n5) / 5
sum = (n1 - media) * (n1 - media)
sum = sum + (n2 - media) * (n2 - media)
sum = sum + (n3 - media) * (n3 - media)
sum = sum + (n4 - media) * (n4 - media)
sum = sum + (n5 - media) * (n5 - media)

desvio = sqrt(sum / 4)
print(desvio)
