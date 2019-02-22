#Escriba un algoritmo que dado el numero de horas trabajadas por un empleado y
#el sueldo por hora, calcule el sueldo total de ese empleado. tenga en cuenta que
#las horas extras se pagana en doble
sueldo_por_hora = 30

horas = int(input("ingrese sus horas laboradas:."))
horas_extras = int(input("ingrese las horas extras laboradas:."))
total = horas * sueldo_por_hora
hrr = (sueldo_por_hora * 2) * horas_extras
print("su total de horas es de :.{}".format(total))
print("su total de horas extras es de :.{}".format(hrr))
