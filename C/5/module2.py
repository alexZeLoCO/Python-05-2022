a = int(input("Numero: "))
# variable es 0 1 o 2
# Cuando sea 0 quiero "Hola"
# Cuando sea 1 quiero "Adios"
# Cuando sea 2 quiero "Hasta luego"
# Cuando sea 3 quiero "Hasta nunca"
# En cualquier otro caso "Numero no valido"

"""
if (a == 0):
    print("Hola") # es 0
else: # si no es 0
    if (a == 1):
        print("Adios") # es 1
    else: # si no es 1
        if (a == 2):
            print ("Hasta luego") # es 2
        else:
            print ("Hasta nunca")
"""

if (a == 0):
    print ("Hola")
elif (a == 1):
    print ("Adios")
elif (a == 2):
    print ("Hasta luego")
elif (a == 3):
    print ("Hasta nunca")
else:
    print ("Numero no valido")
