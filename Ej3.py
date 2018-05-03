class Persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def print_data(self):
        print(self.nombre + ",", self.edad, "años.")
        if self.sexo == "H":
            print("Hombre")
        elif self.sexo == "M":
            print("Mujer")
        else:
            print("Sexo indefinido")
        print(self.peso, "kgs,", self.altura, "cms")
        print("DNI ", self.dni)

    def generar_dni(self):
        import random
        numero = ""
        for i in range(8):
            num = random.randrange(10)
            numero += str(num)
        self.dni = numero
    #Método alternativo que había usado:
    #   from secrets import randbelow
    #   self.dni = (randbelow(90000000) + 10000000)
    #sería  (random menor a 90.000.000) + 10.000.000 (el menor DNI posible)


flaco = Persona("Julio", 22, "H", 62, 182)
assert (flaco.es_mayor_edad() == True)
flaco.print_data()
