##Yostin
##Escriba un algoritmo que dada la cantidad de monedas 5-10-12-5-25-50 cent y
##1 Quetzal, diga cual es la cantidad de dinero que se tiene en total

print("""Ingrese la cantidad de centavos que tenga en monedas de 5,10,15,25,50 centavos
      y 1 Quetzal""")
MO1 = 0.05
MO2 = 0.10
MO3 = 0.15
MO4 = 0.25
MO5 = 0.50
MO6 = 1


mon1 = int(input("Ingrese la cantidad de monedas de 5 centavos"))
mon2 = int(input("Ingrese la cantidad de monedas de 10 centavos"))
mon3 = int(input("Ingrese la cantidad de monedas de 15 centavos"))
mon4 = int(input("Ingrese la cantidad de monedas de 25 centavos"))
mon5 = int(input("Ingrese la cantidad de monedas de 50 centavos"))
mon6 = int(input("Ingrese la cantidad de monedas de 1 Quetzal"))

tot1 = mon1 * MO1
tot2 = mon2 * MO2
tot3 = mon3 * MO3
tot4 = mon4 * MO4
tot5 = mon5 * MO5
tot6 = mon6 * MO6
tot7 = (tot1 + tot2 + tot3 + tot4 + tot5 + tot6)
print("EL total en quetzales es de {}".format(tot7))

