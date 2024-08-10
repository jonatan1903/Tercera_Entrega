class Carta:
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Tréboles"
    PICAS = "Picas"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta1 = Carta(7, Carta.CORAZONES)
carta2 = Carta(6, Carta.PICAS)
carta3 = Carta(11, Carta.TREBOLES)
carta4 = Carta(10, Carta.DIAMANTES)

print("El valor de la carta es: ", carta1.valor ," y su pinta es: ", carta1.pinta)
print("El valor de la carta es: ", carta2.valor ," y su pinta es: ", carta2.pinta)
print("El valor de la carta es: ", carta3.valor ," y su pinta es: ", carta3.pinta)
print("El valor de la carta es: ", carta4.valor ," y su pinta es: ", carta4.pinta)