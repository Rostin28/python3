#moya
#calcular el nuevo salario de un empleado

print ("se le descontara el 20% de su salario")

DES = 0.20
salario = float(input("ingrese su salario:."))
valor = salario * DES
valor1 = salario - valor
print ("el salario a recibir es de:.{}".format(valor1))
print ("se le desconto:.{}".format(valor))

