## Yostin
## 4to ejercicio
## realizar el promedio n notas utilizando el for
n = 0
suma = 0
print ("Bienvenido al progarama:) ".center(50,"*"))

print ("Ingresa la notas las notas que quieras, Ingrese 1 para detener el programa")

cantidad = int(input("ingresa la cantidad de notas q pondras:. "))
for i in range(cantidad):
    n = int(input("ingrese notas :. "))
    suma = suma + n
promedio = suma / cantidad
print("el promedio es:. {}".format(promedio))
