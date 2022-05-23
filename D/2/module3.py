n = int(input("Numero entero mayor que uno: "))

while (n < 1):
    n = int(input("Numero entero mayor que uno: "))

c = 0
for i in range (1, n+1, 1):
    if (n%i == 0):
        c+=1

if (c == 2):
    print(n, "es primo")
else:
    print(n, "no es primo")