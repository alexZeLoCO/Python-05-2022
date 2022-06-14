contador = 0

for i in range (0, int(input("Introduzca cantidad de numeros: ")), 1):
    n=int(input(str("Introduzca numero " + str(i+1) + ": ")))
    if (n < 0):
        contador++

print("Se han introducido", contador, "numeros negativos")