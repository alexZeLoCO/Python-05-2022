# Variables
cantidad = 0
suma = 0
actual = 0

# Entrada
cantidad = int(input("Introduzca la cantidad de numeros a introducir: "))
for i in range (0, cantidad, 1):
    actual = int(input("Introduce numero: "))
    suma+=actual    # suma = suma + actual
print (suma)
