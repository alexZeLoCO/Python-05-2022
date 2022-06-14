suma=0
for i in range (int(input("Introduzca inicio: ")), int(input("Introduzca fin: "))+1, 1):
    suma+=i
print("La suma es:", suma)


print("La suma es:", sum(range(int(input("a: ")), int(input("b: "))+1)))