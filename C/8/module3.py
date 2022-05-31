# Programa que muestre la tabla de multiplicar (desde el 0 hasta el 10) de 'a'
# Se debe pedir 'a' por teclado
"""
Ejemplo:
Introducir a: 2
2x0=0
2x1=2
(...)
2x10=20
"""

# variables
a = 0

# pedir datos
a = int(input("Introducir a: "))

# programa
for i in range(0, 10+1, 1):
    #print(a*i)
    print(a, "x", i, "=", a*i)