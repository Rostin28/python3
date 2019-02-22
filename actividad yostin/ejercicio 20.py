##yostin
##Un maestro desea saber el porcentaje de hombres y el porcentaje de mujeres

print("Desea saber el porcentaje de hombres y de mujeres")

PORC = 100

t = int(input("Ingrese la cantidad total de alumnos:. "))
h = int(input("Ingrese la cantidad de hombres:. "))
m = int(input("Ingrese la cantidad de mujeres:. "))

h1 = (h * PORC)/t
m1 = (m * PORC)/t

print("EL porcentaje de hombres es {}".format(h1))
print("EL porcentaje de mujeres es {}".format(m1))

