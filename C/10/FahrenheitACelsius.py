"""
Programa 13:
    Pide temp en grados Fahrenheit y la escribe en Celsius.
    C = (F - 32) / 1.8

Ejemplo:
    Introduce los grados F: 32
    32 F son 0 C
    50.6 F son 10.334 C
    f, "F son", c, "C"
    F, "F son", C, "C"
"""

# Variables
c = 0
f = 0

# Entrada
#               5    -   ok
#               alex - no ok
#               5.7  - no ok
f = float(input("Introduzca grados F: "))

# Salida
c = (f-32)/1.8

print(f, "F son", c, "C.")