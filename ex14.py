import math

class Circulo():
    def __init__(self, raio):
        self.raio = raio

    def calcular_area (self):
        area = math.pi * self.raio **2
        return area
        
    def calcular_circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        return circunferencia
    
class Cilindro(Circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura
    def calcula_volume(self):
        volume = (math.pi *self.raio **2) * self.altura
        return volume
    
Cilindro_1 = Cilindro(15, 7)

print(round(Cilindro_1.calcular_area(), 2))
print(round(Cilindro_1.calcular_circunferencia(), 2))
print(round(Cilindro_1.calcula_volume(), 2))

Circulo1 = Circulo(10)
print(Circulo1.calcular_area())

    


