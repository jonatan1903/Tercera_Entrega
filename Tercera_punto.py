import math
class plano_cartesiano :

    
    def __init__(self, x, y, X2, y2):
        self.coordenadaX = x
        self.coordenadaY = y
        self.coordenadaX2 = X2
        self.coordenadaY2 = y2
    
    def Movimiento(self, x, y, x2, y2):
        self.coordenadaX += x
        self.coordenadaY += y
        self.coordenadaX2 += x2
        self.coordenadaY2 += y2

    def distancia(self):

        return math.sqrt((self.coordenadaX2 - self.coordenadaX)**2 + (self.coordenadaY2 - self.coordenadaY)**2)

XyY = plano_cartesiano( 5, 3, 4, 2)

distancia_entre_dos_puntos =  XyY.distancia()

print(f" el punto inicialmente está en {XyY.coordenadaX, XyY.coordenadaY} y {XyY.coordenadaX2, XyY.coordenadaY2}")

XyY.Movimiento( 2, 3, 4, 5)     

print(f" Al moverlo quedó en {XyY.coordenadaX, XyY.coordenadaY } y {XyY.coordenadaX2, XyY.coordenadaY2 } ") 

print(f"La distancia entre el punto {XyY.coordenadaX, XyY.coordenadaY} y el punto {XyY.coordenadaX2, XyY.coordenadaY2} es: {distancia_entre_dos_puntos:.3f}")
