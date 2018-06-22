from CapaDatos import *

class CNSocio():
   global cd
   cd = CDSocio()

   def alta(self,s):
       if(self.validaDni(s)== True  and self.validaNombre(s)==True and cd.buscaDNI(s.dni)==0):
            cd.alta(s)
            return True
       else:
           return False

   def borrar(self,s):
       if(self.validaDni(s)== True  and self.validaNombre(s)==True and cd.buscaDNI(s.dni)==1):
           if(cd.borrar(s)==True):
               return True
           else:
               return False
       else:
           return False


   def modificar(self,s):
       if(self.validaDni(s)== True and self.validaNombre(s)==True and cd.buscaDNI == 0):
           socioModif = cd.modificar(s)
           return socioModif
       else:
           return False


   def buscaxId(self,id):
       if (id != ''):
           socEnco = cd.buscarxId(id)
           if socEnco == None:
               return False
           else:
               return socEnco
       else:
           return False

   def todos(self):
       return cd.todos()


   def validaDni(self, s):
       if(s.dni != '' and isinstance(s.dni,int)):
           return True
       else: return False


   def validaNombre(self,s):
       if(isinstance(s.nombre,str) and isinstance(s.apellido,str) and len(s.nombre)<15 and
                            len(s.apellido)<15 and len(s.nombre)>3 and len(s.apellido)>3):
           return True
       else:
           return False


cn = CNSocio()
