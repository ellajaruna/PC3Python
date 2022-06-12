# PREGUNTA 4:

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        pass
    def calcular_area(self):
        area = self.largo * self.ancho
        print(f'El área del rectángulo es: {area}')
        pass

rect1 = Rectangulo(10,8)
print(f'El largo del rectángulo es: {rect1.largo}')
print(f'El anchoo del rectángulo es: {rect1.ancho}')

rect1.calcular_area()

# FIN
