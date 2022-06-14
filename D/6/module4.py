a = int(input("Introduzca numero: "))
b = int(input("Introduzca numero: "))

if (a < b):
    if (a%b==0):
        print(a, "es multiplo de", b)
    else:
        print(a, "no es multiplo de", b)
elif (a > b):
    if (b%a==0):
        print(b, "es multiplo de ",a)
    else:
        print(b, "no es multiplo de", a)
else:
    print("Los dos son iguales")