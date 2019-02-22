##calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre
#su salario actual y un descuento de 2.5% pror servicio
salario = 0
salario_nuevo = 0
incremento = 0.08
salario = int(input("ingrese su salario:."))
incremento = salario * 0.08
salario_nuevo = incremento + salario
descuento = salario_nuevo * 0.025
print("su incremento es de :.{}".format(incremento))
print("su salario_nuevo es de :.{}".format(salario_nuevo))
print("su descuento es de :.{}".format(descuento))
