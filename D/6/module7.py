n = int(input("Introduzca numero: "))
c=0

for i in range (1, n+1, 1):
    if (n%i==0):
        c+=1
if (c==2 and n>2):
    print(n, "es primo")
else:
    print(n,"no es primo")