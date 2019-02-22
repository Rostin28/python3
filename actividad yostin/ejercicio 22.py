##Yostin
##convertir una distancia en metros a pies y pulgadas

PIE = 3.28
PULG = 39.37

print("convertir una distancia en metros a pies y pulgadas")

ing = float(input("Ingresa la cantidad de metros que deseas convertir:. "))
tot = ing * PIE
print("La convercion en PIES es de:. {}".format(tot))
tot2 = ing * PULG
print("La convercion en PULGADAS es de:. {}".format(tot2))
