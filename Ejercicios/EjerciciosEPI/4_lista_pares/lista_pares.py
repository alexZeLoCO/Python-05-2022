"""
Programa que muestre la lista de pares entre dos numeros (ambos incluidos) pedidos por teclado.
Ejemplo:
    Introduzca el primer numero: 10
    Introduzca el segundos numero: 15
    Numeros pares entre 10 y 15:
    10
    12
    14
"""

a = 0
b = 0

a = int(input("Introduzca el primer numero: "))
b = int(input("Introduzca el segundo numero: "))

print ("Numeros pares entre", a, "y", b, ":")
for i in range (a, b+1, 1):
    if (i % 2 == 0):
        print(i)
