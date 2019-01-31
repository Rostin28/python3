##Yostin
##crear un programa que les permita seleccionar entre 1 de 2
##opciones la primera convertir dollares a
##quetzales o convertir quetzales a dollares si es invalida poner opcion invalida
print("Bienvenido al programa".center(50,"*"))

DOLAR = 7.73

print("Seleccione el tipo de convercion q desea 1 para $ a Q o 2 para Q a $")
convercion = int(input("Ingrese 1 o 2 dependiendo de la convercion deseada.: "))
if convercion == 1:
    d = float(input("Ingrese la cantidad de dolares que desea convertir.: "))
    resultado = d * DOLAR
    print("La convercion es Q {}".format(resultado))
elif convercion == 2:
    q = float(input("Ingrese la cantidad de Quetzales que desea convertir.: "))
    resultado2 = q / DOLAR
    print ("La convercion es $ {}".format(resultado2))
else:
    print("DATO INCORRECTO SOLO SE ACPETA 1 U 2")











