"""
 --> Una palabra sin comillas ("") es una variable
 --> Una palabra entre comillas ("") es texto que se muestra tal y como esta

 --> Para unir texto con variables, se utiliza la coma (,). Ejemplo:
    --> print("Nombre", nombre , "y apellidos", apellidos)
                texto , variable, texto       , variable
"""

# DATOS
nombre = "" # guarda el nombre de la persona
edad = 0    # guarda la edad de la persona

# OPERACIONES
# variable = input (pista_para_el_usuario)
nombre = input ("Introducir nombre:") # el usuario pone su nombre
edad = input ("Edad:") # el usuario pone la edad

# RESULTADO
# print (nombre) # mostrar solo el nombre
# print (edad)   # mostrar solo la edad

# Te llamas Alex y tienes 19
print("Te llamas", nombre, "y tienes", edad)
