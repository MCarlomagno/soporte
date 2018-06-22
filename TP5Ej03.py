from TP5Ej02 import *

def buscaDNI(self, dni):
    consulta = "SELECT COUNT(*) FROM socio WHERE dni={0}".format(repr(dni))
    self.conexion.cur.execute(consulta)
    cant = self.conexion.cur.fetchone()
    print("La cantidad de socios con el DNI {0} es {1}".format(dni, cant[0]))
