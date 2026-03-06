print("conozca su consumo de energia")
tuple = ["carlos", "pepe", "nolo", "jairo"]

name = input("inserte su nombre: ")


if name in tuple: 
    ener = float(input("ingrese su consumo en kWh: "))
    dolar = float(0.15)
    print ("el kWh se cobrara a $0.15 por lo que su consumo total sera de: ")
    total = float(ener * dolar)
    print(total, "dolares")
else:
    print("ud no forma parte de nuestros usuarios")