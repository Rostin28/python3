##Yostin
## Solicitar al usuario que selecione una opcion.
## 1) solicitar 2 numeros y elevar el primer numero elevado al 2do numero
## 2) solicitar 3 numeros y elevar el 1ero al 2do y el resultado elevarlo al 3ro

print ("Bienvenido al progarama:) ".center(50,"*"))

opcion = input("Escoge entre 2 opncione 1) para elevar 2 numeros y 2) para elevar 3 numeros entre si ")
if opcion == "1":
   print("ESCOGIO INGRESAR 2 NUMEROS Y ELEVAR EL PRIMERO X EL 2DO")
   n1 = float(input("Ingresa el numero 1:. "))
   n2 = float(input("Ingresa el numero 2:. "))
   elevacion = n1**n2
   print("El resultado es. {}".format(elevacion))
elif opcion == "2":
    print("ESCOGIO INGRESAR 3 NUMEROS Y ELEVARLOS ENTRE SI")
    n1 = float(input("Ingresa el numero 1:. "))
    n2 = float(input("ingresa el numero 2:. "))
    n3 = float(input("ingresa el numero 3:. "))
    elevacion = n1**n2
    elevacion2 = elevacion**n3
    print("El resultado es. {}".format(elevacion2))
else:
    print("OPCION INCORRECTA PRROO")
             









