#Un vendedor recibe un sueldo base mas un 10% extras por comision de sus ventas,
#el vendedor desea saber cuanto dinero obtendra por concepto de comisiones por las
#tres ventas que realiza en el mes y el total que recibira en el mes tomando e cuenta
#su sueldo base y comisiones.
print("su sueldo al mes de de:.2500".center(50,"*"))
sueldo = 2500
comicion = 0.10
ventas = 3
precio_de_ventas = int(input("ingrese precio de su venta:."))
total_de_comicion = (ventas * precio_de_ventas) * comicion
total = sueldo + total_de_comicion
print("el total de comicion es de :.{}".format(total_de_comicion))
print("el total dal mes es de :.{}".format(total))
 
