"""
Programa que retorne la palabra que coincida con las coordenadas introducidas por teclado.
    1       2       3
1   Alfa    Beta    Lambda
2   Beta    Lambda  Alfa
3   Lambda  Alfa    Beta

Ejemplo:
    Introduzca fila: 2
    Introduzca columna: 3
    Alfa
"""

fila = 0
col = 0

fila = int(input("Introduzca fila: "))
col  = int(input("Introduzca columna: "))

if (fila == 1):
    if (col == 1):
        print("Alfa")
    elif (col == 2):
        print("Beta")
    elif (col == 3):
        print("Lambda")
elif(fila == 2):
    if (col == 1):
        print("Beta")
    elif (col == 2):
        print("Lambda")
    elif (col == 3):
        print("Alfa")
elif(fila == 3):
    if (col == 1):
        print("Lambda")
    elif (col == 2):
        print("Alfa")
    elif (col == 3):
        print("Beta")
