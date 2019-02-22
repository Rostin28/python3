##yostin
##Un constructor sabe que necesita 0.5 metros cubicos de arena por metro
##cuadrado de revoque a realalizar. Hacer un programa donde ingrese las medidas
##de un pared (largo y ancho) expresada en metros y obtenga la cantidad de arena
##necesaria para revocar

print("""Un trbajador dencesita 0.5 metros cubicos de arena por metro cuadrado.
      ingrese las medidas de una pared el largo y ancho en metros cuadrados para
      determinar los metros cubicos de arena necesarios""")
METRO2 = 0.5

lar = float(input("Ingrese el largo de la pared en metros cuadrados"))
ancho = float(input("Ingrese el ancho de la parade en metros cuadrados"))

tot1 = (lar * ancho)
tot2 = tot1 * METRO2
print("La cantidad de arena en metros cubicos es de {}".format(tot2))
