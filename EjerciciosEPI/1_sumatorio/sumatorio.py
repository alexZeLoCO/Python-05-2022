"""
Programa que muestre el sumatorio de n numeros. Todos ellos introducidos por el teclado.
n es un numero introducido por teclado tambien.
Ejemplo:
    Introduzca el numero de numeros a introducir: 5
    Introduzca numero: 1
    Introduzca numero: 7
    Introduzca numero: 0
    Introduzca numero: -1
    Introduzca numero: -2
    El sumatorio es: 5
"""

n = 0
numero_actual = 0
suma = 0

n = int(input("Introduzca el numero de numeros a introducir: "))

for i in range (0, n, 1):
    numero_actual = int(input("Introduzca numero: "))
    suma = suma + numero_actual

print("El sumatorio es:", suma)
