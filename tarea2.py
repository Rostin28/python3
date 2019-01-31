##Yostin
##2))solicitar al usuario que escoja 1 de las siguientes opciones 1.sumar 2 numeros 2. restar 3 numeros
##3. multiplicar 4 numero 4.dividir 2 numeros y si el usuario ingresa una opcion invalida hacerselo saber
print("Binevenido al programa :)".center(50,"-"))


print("""Escoja entre las 4 opciones, 1) para sumar 2 numeros, 2) para restar 3 numeros, 3) para multiplicar 4 numeros,
      4) para dividir 2 numeros""")

opcion = int(input("Ingrese 1,2,3 o 4 dependiendo de la opcion que desee:. "))
if opcion == 1:
 print("ESCOGIO SUMAR 2 NUMEROS")
 n1 = float(input("Ingrese el numero 1:. "))
 n2 = float(input("Ingrese el numero 2:. "))
 resultado = n1 + n2
 print("El resultado de la suma es {}".format(resultado))
elif opcion == 2:
    print("ESCOGIO RESTAR 3 NUMERO")
    n3 = float(input("Ingrese el nuemro 1:. "))
    n4 = float(input("Ingrese el numero 2:. "))
    n5 = float(input("Ingrese el numero 3:. "))
    resultado2 = n3 - n4 - n5
    print("El resultado de la resta es {}".format(resultado2))
elif opcion == 3:
    print("ESCOGIO MULTIPLICAR 4 NUMEROS")
    n6 = float(input("Ingresa el numero 1:. "))
    n7 = float(input("Ingresa el numero 2:. "))
    n8 = float(input("Ingresa el numero 3:. "))
    n9 = float(input("Ingresa el numero 4:. "))
    resultado3 = n6 * n7 * n8 * n9
    print("El resultado de la multiplicacion es {}".format(resultado3))
elif opcion == 4:
    print("ESCOGIO DIVIDIR 2 NUMEROS")
    na = float(input("Ingresa el numero 1:. "))
    nb = float(input("Ingresa el numero 2:. "))
    resultado4 = na / nb
    print("El resultado de la division es {}".format(resultado4))
else:
    print("OPCION INCORRECTA EL PROGRAMA SOLO ACEPTA 1,2,3 Y 4 :v")
      
