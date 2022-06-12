# PREGUNTA 3:

from math import pi

class Circulo:
    # Definimos atributo:
    def __init__(self, radio):
        self.radio = radio
        pass
    # Definimoa método:
    def calcular_area(self):
        area = pi * self.radio ** 2
        print(f'El área del círculo es: {round(area,2)}')
        pass

circulo1 = Circulo(5)

print(f'El radio del círculo es: {circulo1.radio}')
circulo1.calcular_area()

# FIN