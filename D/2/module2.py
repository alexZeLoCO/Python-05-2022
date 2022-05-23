# pide un entero y muestra todos los divisores de todos los enteros
# desde el 1 hasta ese

n = int(input("Introduzca entero: "))

for i in range (1, n+1, 1):
    print("Divisores de", i)
    for j in range (1, i+1, 1):
        if (i%j == 0):
            print (j)