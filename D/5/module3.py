suma = 0

for i in range (0, int(input("Introduzca cantidad de numeros: ")), 1):
    suma+=float(input(str("Introduzca numero " + str(i+1) + ": ")))

print("La suma de los numeros que has escrito es:", suma)