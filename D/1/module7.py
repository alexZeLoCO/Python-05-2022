# Variables
a = 0
b = 0

# Entrada
a = int(input("Introduce un numero: "))
b = int(input("Introduce un numero: "))

# Calculo / Algoritmo
if (a>b):
    if(a%b == 0):
        print(a, "es multiplo de", b)
    else:
        print(a, "no es multiplo de", b)
else:
    if(b%a == 0):
        print(b, "es multiplo de", a)
    else:
        print(b, "no es multiplo de", a)

### Opcion 2
##if (a > b):
##    may = a
##    _min = b
##else:
##    may = b
##    _min = a
##
##if (may % _min == 0):
##    print ("Son multiplos")
##else:
##    print ("No son multiplos")