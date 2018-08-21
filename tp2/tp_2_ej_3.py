import random

class Persona(object):
    def __init__(self,sexo,edad,altura):
        self.sexo = sexo
        self.edad = edad
        self.altura = altura
        self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def print_data(self):
        print("sexo: " + self.sexo + "\nedad: " + str(self.edad) + "\naltura: " + str(self.altura) + "\ndni: " + str(self.dni))

    def generar_dni(self):
        numero = ""
        for i in range(8):
            num = random.randrange(10)
            numero += str(num)
        self.dni = numero

a = Persona("m",19,1.85)
