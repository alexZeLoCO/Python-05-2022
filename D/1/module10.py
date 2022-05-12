# Variables
a = 0
b = 0
c = 0

# Entrada
a = int(input("Introduce un numero: "))
b = int(input("Introduce un numero: "))

# Algoritmo
for i in range (a, b+1, 1):
    c = c + i

print(c)