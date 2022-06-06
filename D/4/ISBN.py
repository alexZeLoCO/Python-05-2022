"""
Programa ISBN:
    Crea un ISBN pidiendo al usuario los digitos uno a uno.
    Un ISBN tiene 10 digitos.

Ejemplo:
    Introduzca digito 1: 1
    Introduzca digito 2: 2
    Introduzca digito 3: 3
    (...)
    Introduzca digito 10: 0
    ISBN: 0987654321
"""

ISBN = 0
digito_actual = 0

for i in range (0, 10, 1):
    digito_actual = int(input("Introduzca el digito: "))
    ISBN = ISBN + digito_actual * (10 ** i)

print("ISBN:", ISBN)