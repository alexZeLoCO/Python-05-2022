"""
Programa:
    Pide cuantos numeros va a pedir.
    Pide los numeros.
    Muestra el mayor, el menor y la media de todos.
"""
cantidad = 0 # Cuantos numeros voy a tener
media = 0 # Media de todos los numeros
valor = 0 # Numero actual
mayor = 0 # Mayor numero introducido
menor = 0 # Menor numero introducido

cantidad = int(input("Introduzca la cantidad de numeros a introducir: "))

for i in range (0, cantidad, 1):
    valor = int(input("Introduzca valor: "))
    media = media + valor

    if (valor < menor or i == 0):
        # Si el valor que me dan es mas pequenno que el mas pequenno visto hasta ahora
        # o estamos en la primera vuelta (el primero siempre es el mas pequenno)
        menor = valor # entonces el nuevo mas pequenno es el valor

media = media / cantidad
print("El valor mas pequenno introducido es", menor)
print("La media de los numeros introducidos es", media)


