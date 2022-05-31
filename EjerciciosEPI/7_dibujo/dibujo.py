"""
Programa que pide un tamanno de un triangulo y muestra una figura tal que la siguiente.
Ejemplo:
    Introduzca tamanno del triangulo: 3
    *
    **
    ***
    ***
    **
    *
"""

tamanno = 0

tamanno = int(input("Introduzca tamanno del triangulo: "))

for i in range (0, tamanno, 1):
    for j in range (0, i+1, 1):
        print("*", end = "")
    print()


for i in range (0, tamanno, 1):
    for j in range (0, tamanno-i, 1):
        print("*", end = "")
    print()


         
