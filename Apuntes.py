# /// --- VARIABLES / ENTRADA / SALIDA --- ///
# print(<valor>)
print("Esto sale tal cual")
print(valorDeEstaVariable)
print("El valor de la variable es:", variable)

# <variable> = <valor>
variable = 8
variable = 8+variableDos

# <variable> = input(<texto>)
variable = input("Introduzca texto:")
numero = int(input("Introduzca numero:"))

# /// --- IF / ELIF / ELSE --- ///
# if (<condicion>):
#	<lo que pasa si se cumple>
if (numero > 0):
	print(numero, "es positivo")

# if (<condicion>):
#	<lo que pasa si se cumple>
# else:
#	<lo que pasa si no se cumple>
if (numero > 0):
	print(numero, "es positivo")
else:
	print(numero, "es negativo")

# if (<condicionUno>):
#	<lo que pasa si se cumple>
# elif (<condicionDos>):
#	<lo que pasa si <condicionUno> no se cumple y <condicionDos> si se cumple
if (numero > 0):
	print(numero, "es positivo")
elif (numero % 2 == 0):
	print(numero, "es par")

# if (<condicionUno>):
#	<lo que pasa si se cumple>
# elif (<condicionDos>):
#	<lo que pasa si <condicionUno> no se cumple y <condicionDos> si se cumple
# [se podrian poner tantos elif como sea necesario]
# else:
#	<lo que pasa si no se cumple ninguna de las dos>
if (numero > 0):
	print(numero, "es positivo")
elif (numero % 2 == 0):
	print(numero, "es par")
else:
	print(numero, "no es ni positivo ni par")
	
# /// --- BUCLE FOR --- ///
# for <variable> in range (<inicio>, <fin>, <saltitos>):
#	<lo que se ejecuta en el bucle>
#
# Anotacion:
#   <variable> empezara con valor <inicio> y se le ira sumando <saltitos> hasta llegar a <fin>
for i in range (0, 10, 1):
	if (i%2 == 0):
		print(i, "es par")
	
"""
 /// --- ESTRATEGIAS GENERALES --- ///
 Si un input recibe un numero, se debe utilizar int(input(...))
 Operadores:
   Suma                +
   Resta               -
   Multiplicacion      *
   Division            /
   Modulo / Resto      %
   Asignacion          =
   Comparacion         ==
   Mayor que           >
   Menor que           <
   Mayor o igual que   >=
   Menor o igual que   <=

 Un numero divisible entre otro tiene de resto 0 la division:
 a % b      # El resto de la division a/b
 a % b == 0 # Si el resto de la division a/b es 0 entonces a es multiplo de b
 Los numeros pares son divisibles entre 2
"""