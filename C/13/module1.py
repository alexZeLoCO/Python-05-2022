"""
Programa:
    Pide cantidad de numeros a introducir
    Pide cada numero
    Muestra cuantos negativos se han introducido

Ejemplo:
    Cuantos valores se van a introducir? 2
    Escribe el numero 56
    Escribe el numero -22
    Ha escrito 1 numero negativo
"""

cantidad_numeros = 0
cantidad_valores = 0
negativo = 0

cantidad_numeros = int(input("Cuantos valores se van a introducir? "))
if (cantidad_numeros < 0):
    print("Imposible!")
    cantidad_numeros = int(input("Cuantos valores se van a introducir? "))

for i in range (0, cantidad_numeros, 1):
    cantidad_valores = int(input("Escribe un numero: "))
    if (cantidad_valores < 0):
         negativo = negativo + 1

if (negativo == 1):
    print("Ha escrito", negativo, "numero negativos")
else:
    print("Ha escrito", negativo, "numeros negativos")