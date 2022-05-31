"""
Programa que calcule el area de un circulo, cuadrado o triangulo en funcion de la eleccion del usuario desde un menu.
Todos los datos necesarios seran pedidos por teclado.
"""

opcion = 0

print("Menu. Seleccione una")
print("1. Circulo")
print("2. Cuadrado")
print("3. Triangulo")

opcion = int(input("~> "))

if (opcion == 1):
    radio = int(input("Radio: "))
    print("Area del circulo de radio", radio, "=", radio**2*3.141592654)
elif (opcion == 2):
    lado = int(input("Lado: "))
    print("Area del cuadrado de lado", lado, "=", lado**2)
elif (opcion == 3):
    ladoA = int(input("Lado: "))
    ladoB = int(input("Lado: "))
    print("Area del rectangulo de lados", ladoA, "y", ladoB, "=", ladoA*ladoB)
