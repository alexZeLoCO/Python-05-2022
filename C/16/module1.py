inicio = int(input("Inicio: "))
fin = int(input("Fin: "))
suma = 1
for i in range (inicio, fin+1, 1):
    suma = suma * i
print("La multiplicacion de los numeros desde", inicio, "hasta", fin, "es", suma)