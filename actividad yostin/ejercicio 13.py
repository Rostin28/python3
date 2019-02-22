#Leer dos numeros y encontrar:
#la suma del doble del primero mas el cuadrado del segundo.
#El promedio de su cubos.
n1 = int(input("ingrese n1:."))
n2 = int(input("ingrese n2:."))
suma = n1 + n1
elevacion = n2 ** 2
total = suma + elevacion
print("la total del n1 es de :.{}".format(total))
promedio = (n1 ** 3) + (n2 ** 3)
pro = promedio / 2
print("el promedio es de:.{}".format(pro))
