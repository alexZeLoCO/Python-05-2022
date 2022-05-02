"""
 El programa muestra por pantalla todos los enteros pares desde el 0 hasta
 uno introducido por el usuario (entero)
"""

print("Introduzca un entero positivo:") # Informacion para el usuario

#            input()        ==> Cadena caracteres introducida por usuario
#            int()          ==> Valor entero
#            int(input())   ==> Valor entero introducido por usuario
entero = int(input("Entero: ")) # Recibo valor del usuario

# Mientras el entero sea negativo (no sea positivo)
while (entero < 0):
    # Lo vuelvo a pedir
    print("Err. Se ha introducido un valor negativo. Se necesita un entero positivo")
    entero = int(input("Entero: "))
# Fin del bucle while

# < // ---------- Ahora entero es un entero positivo ---------- // >

print("Se utilizara el numero", entero) # Informacion para el usuario

# Para i=0 hasta i=entero+1 con saltitos de 1...
for i in range (0, entero+1, 1):
    # Si el resto de la division i/2 es 0
    if (i%2==0):
        # Informacion para el usuario
        print("El numero", i, "es par")
    # Fin del if
# Fin del for
#Fin del programa
