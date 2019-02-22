#moya
#calcular el monto del trabajador

print("el presuesto se toma de la siguien manera")
print("sala de urgencia el 37%")
print("sala de pediatria el 42%")
print("sala de traumatologia 21%")
URG = 0.37
PED = 0.42
TRAU = 0.21

presupuesto = float(input("ingrese el presupuesto:."))

valor = float(presupuesto * URG)
valor1 = float(presupuesto * PED)
valor2 = float(presupuesto * TRAU)
print ("el presupuesto para sala de urgencia es de:.{}".format(valor))
print ("el presupuesto para sala de pediatria es de:.{}".format(valor1))
print ("el presupuesto para sala de traumatologia es de:.{}".format(valor2))
