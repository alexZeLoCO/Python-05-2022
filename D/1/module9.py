# Variables
a = 0
b = 0

# Entrada
a = int(input("Introduce un numero: "))
b = int(input("Introduce un numero: "))

# Algoritmo
for i in range (a, b+1, 1):
    if (i%2 == 0):
        print (i, "es par")
