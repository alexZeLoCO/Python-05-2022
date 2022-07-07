"""
3. Programa que revisa si de los 3 numeros introducidos son todos iguales,
solo 2 son iguales o si ninguno es igual.
Introduce un numero: 7
Introduce un numero: 7
Introduce un numero: 7
Todos los numeros son iguales

Introduce un numero: 7
Introduce un numero: 5
Introduce un numero: 7
2 numeros son iguales

Introduce un numero: 7
Introduce un numero: 5
Introduce un numero: 1
Ninguno de los numeros son iguales
"""
n1 = 0
n2 = 0
n3 = 0

n1 = int(input("Introduzca un numero: "))
n2 = int(input("Introduzca un numero: "))
n3 = int(input("Introduzca un numero: "))

if (n1 == n2 and n2 == n3):
    print("a")
else:
    print("b")