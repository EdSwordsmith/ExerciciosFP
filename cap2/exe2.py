km = eval(input("distancia = "))
min = eval(input("tempo = "))

m = km * 1000
h = min / 60
s = min * 60

kmh = km / h
ms = m / s

print("Km/h = ", kmh)
print("m/s = ", ms)
