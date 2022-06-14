actual = int(input("Introduzca anno actual: "))
anno = int(input("Introduzca otro anno: "))

if (actual < anno):
    print("Faltan", anno-actual, "annos para llegar a", anno)
elif (actual > anno):
    print("Han pasado", actual-anno, "annos desde", anno)
else:
    print("Son el mismo anno")