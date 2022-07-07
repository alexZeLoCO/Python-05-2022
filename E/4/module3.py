numero1 = int(input("Introduce tu primer numero: "))
numero2 = int(input("Introduce tu segundo numero: "))
suma = 0
for i in range (numero1, numero2, 1):
    suma = suma + i
print(suma)