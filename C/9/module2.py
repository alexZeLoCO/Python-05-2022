# Pide dos numeros 'a' y 'b'
# Calcula la suma de todos los numeros desde 'a' hasta 'b'
# Muestra la suma
"""
Escribe un numero: 30
Escribe un numero: 32
La suma desde 30 hasta 32 es 93
"""
# Variables
a=0
b=0
c=0
# Pedir datos
a=int(input("Escribe un numero entero: "))
b=int(input("Escribe un numero entero: "))

# Programa / Calculos / Mostrar resultado
for i in range(a,b,1):
    c=c+i