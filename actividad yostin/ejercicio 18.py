##yostin
##Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
## desea saber cuanto debera pagar al final

print("""El cliente desea saber cuanto pagara  de su total de la compra si se
ofrece un descuento del 15% de la misma""")

DESC = 0.15
compra = float(input("Ingrese el total de su compra:. "))
tot = compra * DESC
print("El descuento es de {}".format(tot))
tot2 = compra - tot
print("EL total a pagar es de {}".format(tot2))
