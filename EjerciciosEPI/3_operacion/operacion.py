"""
Programa que haga el siguiente sumatorio: (n^(i+1)/sqrt(i)), siendo n la media de los numeros desde el 0 hasta el 100 -ambos incluidos-.
El sumatorio comienza en 1 y finaliza en un numero introducido por el usuario.
Ejemplo:
    Introduzca el limite del sumatorio: 20
    El sumatorio es: 1.34...
"""

import math

suma = 0
limite = 0
media = 0

limite = int(input("Introduzca el limite del sumatorio: "))

for i in range (0, 101, 1):
    media = media + i

media = media / 100
print(media)
    
for i in range (1, limite+1, 1):
    suma = suma + (media**(i+1)/math.sqrt(i))

print("El sumatorio es:", suma)
