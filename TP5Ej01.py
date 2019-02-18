import pymysql


class ConectarBd():
    def conectar(self):
        global cur,conn
        d=dict()
        d['host']='localhost'
        d['port']=3306
        d['user']='root'
        d['passwd']='root'
        d['db']='proyectosocio'
        self.conn= pymysql.connect(**d)
        self.cur = self.conn.cursor()


class Socio ():
  def __init__(self,idSocio,dni,nombre,apellido):
      self.idSocio=idSocio
      self.dni=dni
      self.nombre=nombre
      self.apellido=apellido
