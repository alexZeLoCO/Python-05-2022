# pide un entero y muestra sus divisores

n = int(input("Entero: "))

for i in range (1, n+1, 1):
    if (n%i == 0):
        print(i)
