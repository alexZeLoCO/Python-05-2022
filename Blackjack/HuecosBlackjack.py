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
    Mas de 21 (sin incluir) ==> Pierde
    Gana el que mas se acerca a 21
    """
    # TODO: Revisa quien ha ganado

mazo = newCartas() # un mazo con todas las cartas

# TODO: Variables

# ---
crupier_original = 0

# TODO: cada jugador empieza con 2 cartas

# ---
crupier = crupier_original
print("Tienes", tu) # mostrar tus cartas

for ronda in range (0, 20, 1):

    # TODO: muestro un 'menu' por pantalla y recojo la eleccion en 'eleccion'
    # Utilizar enteros en el indice para la eleccion

    # ---
    if (2 == eleccion):
        end(tu, crupier) # revisa quien ha ganado
        break   # sale del for
    else:
        tu+=cogerCarta(mazo) # da una carta del mazo
        crupier+=cogerCarta(mazo) # da una carta del mazo
        # TODO: Mostrar tus cartas y crupier_original

        # ---
        if (tu > 21 or crupier > 21):
            end (tu, crupier)
            break   # sale del for

