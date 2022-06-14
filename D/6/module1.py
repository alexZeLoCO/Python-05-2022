a = int(input("Introduzca dividendo: "))
b = int(input("Introduzca divisor: "))
if (b == 0):
    print("No se puede dividir por 0")
elif (a%b == 0):
    print("Division exacta. Cociente:", int(a/b))
else:
    print("Division no exacta. Cociente:", int(a/b), "Resto:", a%b)