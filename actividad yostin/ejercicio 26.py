##yostin
##Un programa q pida 3 numeros positivos y que muestre la suma,resta y multiplicacion
## de todos El resultado deve ser siempre positivo
resta = 0

print("Ingrese 2 numeros ENTEROS POSITIVOS y se mostrara la +,- y * de estos")

num1 = int(input("Ingrese el numero 1:. "))
num2 = int(input("Ingrese el numero 2:. "))
num3 = int(input("Ingrese el numero 3:. "))

if num1 >=0 and num2 >=0 and num3 >=0:
    suma = num1 + num2 + num3
    multi = num1 * num2 * num3
    resta = num1 - num2 - num3
    print("La suma de los 3 numeros es de:. {}".format(suma))
    print("La multiplicacion de los 3 numeros es de:. {}".format(multi))
    if resta >=0:
          print("La resta de los 3 numeros es de:. {}".format(resta))
    elif resta <0:
        print("La resta es negativa")

else:
    print("solo numeros positivos")
