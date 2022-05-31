"""
Programa que muestra la suma de todos los divisores de un numero introducido por el teclado.
Ejemplo:
Introduzca un numero: 22
La suma de todos los divisores de 22 es 36
"""

n = 0
suma = 0

n = int(input("Introduzca un numero: "))

for i in range(1, n+1, 1):
    if (n % i == 0):
        suma = suma + i

print("La suma de todos los divisores de", n, "es", suma)
