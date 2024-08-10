class carro:
    
    def __init__(self, Velocidad_maxima, kilometraje) :
        self.velocidad_maxima = Velocidad_maxima
        self.kilometraje = kilometraje


carro1 = carro("200 km/h", "2000 km") 

print(carro1.velocidad_maxima)
print(carro1.kilometraje)