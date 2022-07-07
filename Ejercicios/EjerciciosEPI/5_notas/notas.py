"""
Programa que muestre la nota en funcion del valor de la misma.
Ejemplo:
    Introducir nota: 7.5
    Notable

----
Suspenso            --> [0, 5)
Aprobado            --> [5, 7)
Notable             --> [7, 9)
Matricula de Honor  --> [9, 10]
"""

nota = 0

nota = float(input("Introduzca nota: "))

if (nota < 5):
    print("Suspenso")
elif (nota < 7):
    print("Aprobado")
elif (nota < 9):
    print("Notable")
else:
    print("Matricula de Honor")
