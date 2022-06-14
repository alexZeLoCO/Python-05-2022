cantidad = int(input("Cantidad de numeros: "))
numero = 0
suma = 0
sumatorio = 0
for i in range (0, cantidad, 1):
    numero = int(input("Introduzca numero: "))
    if (numero > suma/(i+1) or i==0):
        sumatorio = sumatorio + numero
    elif (previo != 0 and numero % previo == 0):
        sumatorio = sumatorio - numero
    suma = suma + numero
    previo = numero

print(sumatorio)