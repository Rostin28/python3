##yostin
##Calcular el cambio de moneda en dolares y euros al ingresar cierta cantidad
## en Q (tipo de cambio $=2150, Euros = 1.45
print ("""Calcular el cambio de moneda en dolares y euros al ingresar cierta cantidad
 en Q (tipo de cambio $=2150 E, Euros = 1.45 D """)


DOLARES = 1.45
EUROS = 2150


totl = float(input("Ingresa tu cantidad  pasarlos a Dolares y Euros:. "))
total = totl * DOLARES
print("EL Cambio de  dolares es de {}".format(total))
total2 = totl * EUROS
print("El cambio de Euros es de {}".format(total2))


