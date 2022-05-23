import random

def newCartas ():
    """
    Crea un mazo de cartas
    [[<valorCarta>, <cantidad>],
     [<valorCarta>, <cantidad>],
     (...)
    ]
    """
    cartas = [] # mazo vacio
    for i in range (1, 11, 1): # para cada carta
        cartas.append([i, 4]) # incluir 4 cartas en mazo
    return cartas # retornar mazo

def available (carta, mazo):
    """
    Revisa si la carta esta en el mazo
    """
    return mazo[carta-1][1] != 0

def remove (carta, mazo):
    """
    Elimina una carta del mazo
    """
    mazo[carta-1][1] = mazo[carta-1][1] -1

def cogerCarta (mazo):
    """
    Recibe una carta nueva del mazo.
    Revisa que se puede coger esa carta.
    Si no se puede, coge otra hasta que se pueda.
    """
    carta = random.randint(1, 10) # carta aleatoria
    while (not available(carta, mazo)): # mientras no se pueda coger (no quedan)
        carta = random.randint(1, 10) # carta aleatoria
    remove(carta, mazo) # eliminar carta del mazo
    return carta # retornar carta

def end (tu, crupier):
    """
    Revisa quien ha ganado
    """
    tu_total = total(tu)
    crupier_total = total(crupier)
    if (tu_total > 21): # pierdes
        print("Tienes mas de 21. Has perdido! (Crupier:", crupier, ")")
    elif (crupier_total > 21): # ganas
        print("El crupier tiene mas de 21. Has ganado! (Crupier:", crupier, ")")
    elif (tu_total > crupier_total): # ganas
        print("Tienes mas que el crupier (", tu, ">", crupier, "). Has ganado!")
    elif (crupier_total > tu_total): # pierdes
        print("El crupier tiene mas que tu (", crupier, ">", tu, "). Has perdido!")
    else: # empate
        print("Empate! (", crupier,")")

def total (cartas):
    out = 0
    for i in range (0, len(cartas), 1):
        out = out + cartas[i]
    return out

mazo = newCartas() # un mazo con todas las cartas

tu = []
crupier = []

# cada jugador empieza con 2 cartas
for i in range (0, 2, 1):
    tu.append(cogerCarta(mazo)) # carta aleatoria para jugador
    crupier.append(cogerCarta(mazo)) # carta aleatoria para crupier

print("Tienes", total(tu)) # mostrar tus cartas

for ronda in range (0, 20, 1):

    # muestro un 'menu' por pantalla
    print("Seleccionar numero:")
    print("1. Coger carta")
    print("2. Parar")

    eleccion = int(input("~> ")) # eleccion del jugador

    if (2 == eleccion):
        end(tu, crupier) # revisa quien ha ganado
        break   # sale del for
    else:
        tu.append(cogerCarta(mazo)) # carta aleatoria para jugador
        crupier.append(cogerCarta(mazo)) # carta aleatoria para crupier
        print("Tienes", total(tu)) # mostrar tus cartas
        if (total(tu) >= 21 or total(crupier) >= 21):
            end(tu, crupier) # revisa quien ha ganado
            break   # sale del for

