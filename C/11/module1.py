"""
Programa 3:
    Pide anno actual y otro cualquiera.
    Mostrar cuantos annos han pasado desde el otro o cuantos faltan.

¿En que anno estamos?: 2015 # NOTA: El acutal es menor que el otro
Escribe un anno cualquiera: 2020
Para llegar al 2020 faltan 5 annos

¿En que anno estamos?: 2015 # NOTA: El acutal es mayor que el otro
Escribe un anno cualquiera: 1997
Desde el anno 1997 han pasado 18 annos

¿En que anno estamos?: 2015 # NOTA: El acutal es igual que el otro
Escribe un anno cualquiera: 2015
¡Son el mismo anno!
"""

# Variables
actual = 0 # Entrada
otro = 0 # Entrada
diferencia = 0 # Resultado

# Entrada
actual = int(input("¿En que anno estamos?: "))
otro = int(input("Escribe un anno cualquiera: "))

# Salida
if (actual < otro):
    diferencia = otro - actual
    print("para llegar al", otro, "faltan", diferencia, "annos")
elif (otro < actual):
    diferencia = actual - otro
    print("Desde el anno", otro, "han pasado", diferencia, "annos")
else:
    print("¡Son el mismo anno!")
