import math

class Rectangulo:
    def __init__(self, x1, y1, x2, y2):
        self.coordenadax1 = x1
        self.coordenaday1 = y1
        self.coordenadax2 = x2
        self.coordenaday2 = y2

    def calcular_perimetro(self):
        largo = abs(self.coordenadax2 - self.coordenadax1)
        ancho = abs(self.coordenaday2 - self.coordenaday1)
        return 2 * (largo + ancho)

    def calcular_area(self):
        largo = abs(self.coordenadax2 - self.coordenadax1)
        ancho = abs(self.coordenaday2 - self.coordenaday1)
        return largo * ancho

    def es_cuadrado(self):
        largo = abs(self.coordenadax2 - self.coordenadax1)
        ancho = abs(self.coordenaday2 - self.coordenaday1)
        return largo == ancho

rectangulo = Rectangulo(4, 20, 3, 5)

print(f"Perímetro: {rectangulo.calcular_perimetro()}")
print(f"Área: {rectangulo.calcular_area()}")
print(f"Es un cuadrado: {'Sí' if rectangulo.es_cuadrado() else 'No'}")
