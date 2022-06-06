"""
Programa 5:
    Pide 3 numeros.
    Muestra si los 3 son iguales, 2 iguales o ninguno.

Escribe un numero: 6
Escribe otro numero: 6
Escribe otro numero mas: 6
Has escrito tres veces el mismo numero.

Escribe un numero: 6
Escribe otro numero: 6.5
Escribe otro numero mas: 6
Has escrito uno de los numeros dos veces.

Escribe un numero: 4
Escribe otro numero: 5
Escribe otro numero mas: 6
Los tres numeros que has escrito son distintos
"""
n1 = 0
n2 = 0
n3 = 0

n1 = int(input("Escribe un numero: "))
n2 = int(input("Escribe otro numero: "))
n3 = int(input("Escribe otro numero mas: "))

if (n1 == n2 and n3 == n1):
    print ("Has escrito tres veces el mismo numero.")
elif (n1 == n2 or n3 == n1 or n2 == n3):
    print ("Has escrito uno de los numeros dos veces.")
else:
    print ("Los tres numeros que has escrito son distintos.")