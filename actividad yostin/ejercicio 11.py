##yostin
## un programa donde se ingrese el tiempo en horas, minutos y segundos y se
## calcule el tiempo necesario sabiendo que el costo x segundo es de 0.25

print("""Ingrese el tiempo necesario en horas, minutos y seg sabiendo q el costo
es de 0.25 por segundo""")

COST_X_SEG = 0.25


hr = float(input("Ingrese el tiempo en horas:. "))
minn = float(input("Ingrese el tiempo en minutos:. "))
seg = float(input("Ingrese el tiempo en segundos:. "))

cost = seg / COST_X_SEG
cost2 = (minn * 60)/COST_X_SEG
cost4 = (hr * 3600)/COST_X_SEG
total = cost + cost2 + cost4
print("EL total es {}".format(total))
