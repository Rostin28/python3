##Yostin
##Elabore un programa que lea 2 numeros enteros positivos y que muestre la suma
##la resta y la multiplicacion de estos

print("Ingrese 2 numeros ENTEROS POSITIVOS y se mostrara la + y * de estos")

num1 = int(input("Ingrese el numero 1:. "))
num2 = int(input("Ingrese el numero 2:. "))

if num1 >=0 and num2 >=0:
    suma = num1 + num2
    multi = num1 * num2
    print("La suma de los 2 numeros es de:. {}".format(suma))
    print("La multiplicacion de los 2 numeros es de:. {}".format(multi))
else:
    print("solo numeros positivos")
