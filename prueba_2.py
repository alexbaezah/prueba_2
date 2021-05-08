estudiante = False

nombre = input("indíqueme su nombre ")

edad = int(input("indique su edad "))
if edad < 18:
    edad = True  
else: 
    edad = False

estudiante = input("¿es usted estudiante? si/no ")
if estudiante == "si":
    estudiante = True 
elif estudiante == "no":
    estudiante = False 

if edad:
    print(f"Usted {nombre} al ser menor de edad, el costo de entrada al cerro es de 1.000 pesos")
else:
    print(f"Usted {nombre} al ser ayor de edad el costo de entrada al cerro es de 2.000 pesos ")

monto_total = 0

print("para beber.... \n1) Café o té -> $1.000\n2)Mote con huesillo -> $.1500\n3)Jugo Natural -> $2.000")
bebida = int(input("ingrese la opción que desea llevar "))
cantidad = int(input("¿Cuánto llevará? "))
if bebida == 1:
    cantidad *= 1000
    monto_total = cantidad
elif bebida == 2:
    cantidad *= 1500
    monto_total = cantidad
elif bebida == 3:
    cantidad *= 2000
    monto_total = cantidad 


print(f"el monto comprado en bebidas fue: ${monto_total}")

print("para comer.... \n1) Barra de proteína -> $1.000\n2)Sandwich de jamón o queso -> $.1500\n3)Sandwich de palta -> $2.000")
comer = int(input())
cantidad = int(input("¿Cuánto llevará ?"))
if comer == 1:
    cantidad *= 1000
    monto_total += cantidad
elif comer == 2:
    cantidad *= 1500
    monto_total += cantidad
elif comer == 3:
    cantidad *= 2000
    monto_total += cantidad 

print(f"el monto total comprado entre bebida y comida es: ${monto_total}")

if estudiante:
    descuento = monto_total * 0.5 
    monto_total -= descuento
    print(f"el monto total comprado entre bebida y comida con descuento de 50% por ser estudiante es: ${monto_total:.0f}")
    efectivo = int(input("¿con cuánto pagará ?"))
    vuelto = efectivo - monto_total 
    if efectivo < monto_total:
        print("no hay vuelto y tampoco hay venta")
    elif efectivo == monto_total:
        print("pagó con el monto justo, no hay vuelto")
    else:
        print(f"su vuelto es de {vuelto:.0f}")
else: 
    efectivo = int(input("¿con cuánto pagará ?"))
    vuelto = efectivo - monto_total 
    if efectivo < monto_total:
        print("no hay vuelto y tampoco hay venta")
    elif efectivo == monto_total:
        print("pagó con el monto justo, no hay vuelto")
    else:
        print(f"su vuelto es de {vuelto:.0f}")



