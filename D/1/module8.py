# Variables
a = 0
b = 0
c = 0

# Entrada
a = int(input("Introduzca un numero: "))
b = int(input("Introduzca un numero: "))
c = int(input("Introduzca un numero: "))

# Algoritmo
if (a == b or a == c or b == c):
    if (a == b and a == c):
        print ("Son iguales")
    else:
        print ("2 son iguales")
else:
    print ("No son iguales")
