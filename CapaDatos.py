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
class CDSocio ():
   def __init__(self):
      self.conexion = ConectarBd()
      a = self.conexion.conectar()

   def alta(self,socioAlta):
      consulta1="insert into socio (dni,nombre,apellido) values({0},{1},{2})"\
          .format(repr(socioAlta.dni), repr(socioAlta.nombre),repr(socioAlta.apellido))
      self.conexion.cur.execute(consulta1)
      self.conexion.conn.commit()
      a = self.conexion.cur.lastrowid
      print("El socio fue agregado correctamente y su Id es: {0}".format(a))
      return self.conexion.cur.lastrowid

   def borrar(self,socioBorrar):
       consulta2="delete from socio where idsocio = %d" %socioBorrar.idSocio
       self.conexion.cur.execute(consulta2)
       self.conexion.conn.commit()
       if self.conexion.cur.rowcount == 0:
           return False
       else:
           return True

   def modificar(self,socioModificar):
       consulta3='update socio  set dni={0}, nombre={1}, apellido={2} where idsocio = {3}'\
           .format(repr(socioModificar.dni), repr(socioModificar.nombre),
                   repr(socioModificar.apellido), socioModificar.idSocio)
       self.conexion.cur.execute(consulta3)
       self.conexion.conn.commit()
       return socioModificar

   def buscarxId(self,idSocio):
       consulta4='select * from socio where idsocio=%d' %idSocio
       self.conexion.cur.execute(consulta4)
       socioEnco=self.conexion.cur.fetchone()
       print (socioEnco[0],socioEnco[1],socioEnco[2], socioEnco[3])
       return socioEnco

   def todos(self):
       consulta5 = "SELECT * FROM socio"
       self.conexion.cur.execute(consulta5)
       socios = self.conexion.cur.fetchall()
       for i in socios:
           print (i[0],i[1],i[2],i[3])

   def buscaDNI(self, dni):
        consulta = "SELECT COUNT(*) FROM socio WHERE dni={0}".format(repr(dni))
        self.conexion.cur.execute(consulta)
        cant = self.conexion.cur.rowcount
        if cant == 0:
           return 0
        else:
           return 1
