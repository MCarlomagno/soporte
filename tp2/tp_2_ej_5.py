from tp_2_ej_4 import Estudiante

a = Estudiante("m",23,1.75,"ingenieria en sistemas",2014, 35, 20)
b = Estudiante("m",23,1.75,"ingenieria en sistemas",2014, 35, 20)
c = Estudiante("m",23,1.75,"ingenieria nuclear",2014, 35, 20)
d = Estudiante("m",23,1.75,"ingenieria nuclear",2014, 35, 20)

lista_estudiantes = [a,b,c,d]

def estudiantes_x_carrera(lista_estudiantes):
    dic = {}
    for est in lista_estudiantes:
        if est.nombre_carrera in dic:
            dic[est.nombre_carrera] += 1
        else:
            dic[est.nombre_carrera] = 1
    return dic

print(estudiantes_x_carrera(lista_estudiantes))
