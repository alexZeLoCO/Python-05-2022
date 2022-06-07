"""
Programa:
    Pide un numero de numeros a pedir.
    Pide cada numero (pueden ser decimales).
    Muestra la suma de todos

Ejemplo:
    ¿Cuantos vas a introducir? 5
    Escribe numero 1: 25
    Escribe numero 2: 30
    (...)
    La suma de los numeros que has escrito es 102.5
"""
# Variables
cantidad_numeros = 0    # cantidad de numeros que se van a introducir (pedir)
decimales = 0           # numero individual que se pide
suma = 0                # suma de los decimales introducidos

# Entrada
cantidad_numeros = int(input("¿Cuantos valores vas a introducir? "))
for i in range (0, cantidad_numeros, 1):
    decimales = int(input("Escribe el numero: "))

test = 0
print("test")
