#moya
#calcular el monto de una cabina wifi
print ("el precio por hora es de 1.5 pero si estas 5 horas tendras una hora gratis")

BS = 1.5
hr = float(input("ingrese el tiempo que estara:."))
if hr > 0 and hr < 5:
    total = (BS * hr)
    print ("tu precio a pagar es:.{}".format(total))
elif hr >= 5:
    total = BS * hr
    print ("tienes que pagar:.{}".format(total))
    if hr >=5:
        total2 = hr / 5
        print("LAS HORAS GRATIS Q TIENES SON")
        print(int(total2))
