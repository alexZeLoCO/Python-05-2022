"""
Introduce un numero par: 2
Los 3 pares siguientes son:
2
4
6
"""
par = int(input("Introduce un numero par: "))
# primer par: par
# segundo par: par+2
# tercer par: par+4
for i in range (par, par+4, 2):
    print(i)
