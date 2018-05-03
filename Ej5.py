from Ej4 import Estudiante


def estudiantes_x_carrera(lista_estudiantes):
    dic = {}
    for est in lista_estudiantes:
        if est.nombre_carrera in dic:
            dic[est.nombre_carrera] += 1
        else:
            dic[est.nombre_carrera] = 1
    return dic


a = Estudiante("Marcos", 23, "H", 60, 175, "Ingeniería en Sistemas de Información", 2014, 35, 20)
b = Estudiante("Julio", 22, "H", 72, 182, "Ingeniería en Sistemas de Información", 2014, 35, 16)
c = Estudiante("Einstein", 76, "H", 82, 170, "Doctorado en Física", 2014, 25, 18)
d = Estudiante("Curie", 18, "M", 67, 160, "Ingeniería Nuclear", 2014, 50, 48)
lista_estudiantes = [a, b, c, d]
print(estudiantes_x_carrera(lista_estudiantes))
