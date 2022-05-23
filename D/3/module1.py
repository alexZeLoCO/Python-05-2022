AA = 0
AB = 0
AC = 0
BA = 0
BB = 0
BC = 0
CA = 0
CB = 0
CC = 0

ganador = False
err = False
n_Errores = 0

casillasUno = 0
casillasDos = 0

for i in range (0, 9, 1):
    err = False

    print(AA, AB, AC)
    print(BA, BB, BC)
    print(CA, CB, CC)
    print("Jugador", (i-n_Errores)%2+1)
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))

    if (fila == 1):
        if (columna == 1 and AA == 0):
            AA = (i-n_Errores)%2+1
        elif (columna == 2 and AB == 0):
            AB = (i-n_Errores)%2+1
        elif (columna == 3 and AC == 0):
            AC = (i-n_Errores)%2+1
        else:
            err = True
    elif (fila == 2):
        if (columna == 1 and BA == 0):
            BA = (i-n_Errores)%2+1
        elif (columna == 2 and BB == 0):
            BB = (i-n_Errores)%2+1
        elif (columna == 3 and BC == 0):
            BC = (i-n_Errores)%2+1
        else:
            err = True
    elif (fila == 3):
        if (columna == 1 and CA == 0):
            CA = (i-n_Errores)%2+1
        elif (columna == 2 and CB == 0):
            CB = (i-n_Errores)%2+1
        elif (columna == 3 and CC == 0):
            CC = (i-n_Errores)%2+1
        else:
            err = True
    else:
        err = True

    if (AA == AB and AB == AC and AA != 0):
        print("Gano", AA)
        ganador = True
        break
    if (BA == BB and BB == BC and BA != 0):
        print("Gano", BA)
        ganador = True
        break
    if (CA == CB and CB == CC and CA != 0):
        print("Gano", CA)
        ganador = True
        break
    if (AA == BA and CA == CA and AA != 0):
        print("Gano", AA)
        ganador = True
        break
    if (AB == BB and CB == CB and AB != 0):
        print("Gano", AB)
        ganador = True
        break
    if (AC == BC and BC == CC and AC != 0):
        print("Gano", AC)
        ganador = True
        break

    if (err):
        n_Errores+=1
    else:
        n_errores = 0

    if ((i-n_errores)%2+1 == 1):
        casillasUno+=1
    else:
        casillasDos+=1

print(AA, AB, AC)
print(BA, BB, BC)
print(CA, CB, CC)

if (not ganador):
    print("Empate")

print("Casillas jugador 1:", casillasUno)
print("Casillas jugador 2:", casillasDos)