#moya
#el descuento ey el monto a pagar por un medicamento

print ("el descuento es del 35% para cada medicamento")

DES = 0.35
precio = float(input("ingrese precio del medicamento:."))
can = (precio * DES)
can1 = (precio - can)
print ("el descuento que se le aplico es de:.{}".format(can))
print ("el precio que tiene que pagar ya con descuento es de:.{}".format(can1))
