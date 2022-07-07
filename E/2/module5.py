"""
Introduce año actual: 2022
Introduce año de nacimiento: 2002
Eres mayor de edad porque tienes 19 años.
----
Introduce año actual: 2022
Introduce año de nacimiento: 2020
Eres menor de edad porque tienes 2 años.
"""
actual = int(input("Introduzca año actual: "))
nacimiento = int(input("Introduzca año de nacimiento: "))
if (actual-nacimiento >= 18):
    print("Eres mayor de edad porque tienes", actual-nacimiento, "años")
else:
    print("Eres menor de edad porque tienes", actual-nacimiento, "años")
