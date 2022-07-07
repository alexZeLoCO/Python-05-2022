def resto (a, b):
    return a%b

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
resto = n1%n2

if (resto(n1, n2) == 0 or resto(n2, n1) == 0):
    print("Son divisibles")
else:
    print("No son divisibles")