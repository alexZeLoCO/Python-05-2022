"""
Programa biseccion:
    Pide un numero de iteraciones.
    Repite el siguiente algoritmo
        si f(a) * f((b+a)/2) < 0 entonces raiz en [a, (b+a)/2]
        si no raiz en [(b+a)/2, b]

    Ejemplo:
        Itroduzca numero de iteraciones: 10
        La raiz de la funcion es ____ y su valor aproximado f(x) es ____
"""

def f (x):
    """
    Funcion a utilizar.
    USO: f(x)
    """
    return -x**5 + 2*x**4 - 3*x**3 + 4*x**2 - 5*x + 7
