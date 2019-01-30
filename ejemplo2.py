##Yostin
## calcular la edad actual de una persona, previamente ingresando el año
##- actual y el año de nacimiento
print("Binevenido al programa".center(50,"*"))
FEC_ACT = 2019
fec_nacimiento = int(input("Ingresa tu año de nacimiento.: "))

edad = FEC_ACT - fec_nacimiento

print("Tu edad es {}".format(edad))

if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")






