"""
Introduce numero inicial: 2
Introduce numero final: 5
2
3
4
5
"""
# variable inicial: primer numero que se debe mostrar
# variable final:   ultimo numero que se debe mostrar
inicial = int(input("Introduce numero inicial: "))
final = int(input("Introduce numero final: "))

for i in range (inicial, final+1, 1):
    print(i)
