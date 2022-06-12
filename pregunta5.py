# PREGUNTA 5:

class Alumno:
    def __init__(self,nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        pass

    def display(self):
        print(f'''Información del estudiante:\nNombre: {self.nombre}\nNúmero de registro: {self.numero_registro}''')
        pass

    def setAge(self, edad):
        print(f'La edad del estrudiante es: {edad}')
        pass

    def setNota(self, nota1, nota2, nota3):
        print(f'Las notas del estudiante son: {nota1} , {nota2} y {nota3}')
        pass

alum1 = Alumno('Juan',1514569)

alum1.display()
alum1.setAge(20)
alum1.setNota(15, 16, 18)

# FIN