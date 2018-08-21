from tp_2_ej_3 import Persona

class Estudiante(Persona):
    def __init__(self,sexo,edad,altura,nombre_carrera, ano_ingreso, num_materias, num_materias_aprob):
        Persona.__init__(self,sexo,edad,altura)
        self.nombre_carrera = nombre_carrera
        self.ano_ingreso = ano_ingreso
        self.num_materias = num_materias
        self.num_materias_aprob = num_materias_aprob

    def avance(self):
        proporcion = self.num_materias_aprob / float(self.num_materias)
        porcentaje = proporcion*100
        print(str(porcentaje) + "%")

    def edad_ingreso(self):
        cant_anos = 2018 - self.ano_ingreso
        edad_ingreso = self.edad - cant_anos
        print(edad_ingreso)

marcos = Estudiante("m",23,1.75,"ingenieria en sistemas",2014, 35, 20)

marcos.avance()
marcos.edad_ingreso()
