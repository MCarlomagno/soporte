from Ej3 import Persona


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, peso, altura, nombre_carrera, ano_ingreso, num_materias, num_materias_aprob):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.nombre_carrera = nombre_carrera
        self.ano_ingreso = ano_ingreso
        self.num_materias = num_materias
        self.num_materias_aprob = num_materias_aprob

    def avance(self):
        proporcion = self.num_materias_aprob / self.num_materias
        porcentaje = round(proporcion*100, 2)
        print(str(porcentaje) + "% de la carrera completada.")

    def edad_ingreso(self):
        cant_anos = 2018 - self.ano_ingreso
        edad_ingreso = self.edad - cant_anos
        print("Ingresó con " + str(edad_ingreso) + " años.")


flaco = Estudiante("Julio", 22, "H", 62, 182, "Ingeniería en Sistemas de Información", 2014, 35, 20)
flaco.avance()
flaco.edad_ingreso()
