## yostin
## 3er ejercicio
## realizar el promedio de 5 notas utilizando el ciclo for


suma = 0
print("Bienvenido al programa".center(10,"*"))
print ( " Ingresa 5 notas para saar su promedio")

for i in range(5):
    n = int(input("ingrese notas :. "))
    suma = suma + n
promedio = suma / 5 
print("el promedio es:. {}".format(promedio))
