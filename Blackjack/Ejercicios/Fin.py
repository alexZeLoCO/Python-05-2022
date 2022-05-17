tu = 0
crupier = 0

if (tu > 21):
    print("Tienes mas de 21 (", tu, "). Has perdido! (Crupier:", crupier, ")")
elif (crupier > 21):
    print("El crupier tiene mas de 21 (", crupier, "). Has ganado! (Tu:", tu, ")")
elif (tu > crupier):
    print("Tienes mas que el crupier (", tu, ">", crupier, "). Has ganado!")
elif (crupier > tu):
    print("El crupier tiene mas que tu (", crupier, ">", tu, "). Has perdido!")
else:
    print ("Empate! (", crupier, ")")
