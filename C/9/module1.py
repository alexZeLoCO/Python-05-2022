# Programa pide kg y altura.
# Calcular IMC = kg / (altura * 2)
# Mostrar el IMC
"""
Introducir peso (kg): 10
Introducir altura (m): 200
IMC: 5
"""

# Variables
kg=0
altura=0
imc=0
# Pedir datos
kg=int(input ("Introducir peso (kg): "))
altura =int (input("Introducir altura (m): "))
# Programa / Calculos / Mostrar resultados
imc=kg/(altura*2)
print ("IMC:", imc)