horas = eval(input("horas = "))
sal_hora = eval(input("salario hora = "))

if horas <= 40:
    print(horas * sal_hora)
else:
    print(sal_hora * 40 + (horas - 40) * 2 * sal_hora)