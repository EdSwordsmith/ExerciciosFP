sec = eval(input("sec = "))

min = sec // 60
sec = sec % 60

horas = min // 60
min = min % 60

dias = horas // 24
horas = horas % 24

print("dias: ", dias, " h: ", horas, " min: ", min, " sec: ", sec)
