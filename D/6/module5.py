a = float(input("Introduzca numero: "))
b = float(input("Introduzca numero: "))
c = float(input("Introduzca numero: "))

if (a == b and b == c):
    print("Los 3 son iguales")
elif (a == b or b == c or a == c):
    print("Hay 2 que son iguales0")
else:
    print("Todos son distintos")
