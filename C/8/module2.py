"""
for i in range (<inicio>, <fin>, <saltitos>):
    <ordenes a repetir>
"""

# Un programa que muestra los numeros desde 'a' hasta 'b'.
# Tiene que pedir 'a' y 'b' por el teclado.
# Se supone que 'a' < 'b'

# Variables
a = 0
b = 0

# Pedir datos
a = int(input("Introducir a: "))
b = int(input("Introducir b: "))

# Programa
for i in range(a, b+1, 1):
    print(i)