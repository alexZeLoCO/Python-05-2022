"""
0 0 0
0 0 0
0 0 0

Jugador 1: 1
Jugador 2: 2

1 0 2
0 2 0
1 0 1
    Columna
    1  2  3
F 1 AA AB AC
I 2 BA BB BC
L 3 CA CB CC
A
"""
# variable = valor
# variable = 0
# AA = 0
AA = 0
AB = 0
AC = 0
BA = 0
BB = 0
BC = 0
CA = 0
CB = 0
CC = 0

print (AA, AB, AC)
print (BA, BB, BC)
print (CA, CB, CC)

fila = 0    # fila en la que va la marca
columna = 0 # columna en la que va la marca

fila = int(input("Fila: "))
columna = int(input("Columna: "))

# posibles valores de fila: 1 2 3
# posibles valores de colu: 1 2 3

# si fila es 1 entonces me refiero a la primera
if (fila == 1):
    if (columna == 1):
        AA = 1
    elif (columna == 2):
        AB = 1
    elif (columna == 3):
        AC = 1
elif (fila == 2):
    if (columna == 1):
        BA = 1
    elif (columna == 2):
        BB = 1
    elif (columna == 3):
        BC = 1
elif (fila == 3):
    if (columna == 1):
        CA = 1
    elif (columna == 2):
        CB = 1
    elif (columan == 3):
        CC = 1

    print (AA, AB, AC, BA, BB, BC, CA, CB, CC)
