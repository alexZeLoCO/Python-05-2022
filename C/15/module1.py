# 3 variables. Inicio. Fin. Suma

suma=0
for i in range (int(input("Introduzca inicio: ")), int(input("Introduzca fin: "))+1, 1):
    suma+=int(input("Introduzca numero: "))
print("La suma es:", suma)
