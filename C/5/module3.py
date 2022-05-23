# Programa recibe un numero en 'n' del teclado ok
# Si es par dice "es par" ok
# Si no, dice "no es par"

n = int(input("Numero: "))
m = int(input("Multiplos de: "))

if (n%m == 0):
    print("es multiplo")
else:
    print ("no es multiplo")