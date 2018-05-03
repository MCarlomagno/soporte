import datetime


class Persona:
    def __init__(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def edad(self):
        fecha_actual = datetime.datetime.now()
        self.edad = (fecha_actual - self.fecha_nacimiento)
        self.edad = self.edad.days
        self.edad = round(self.edad / 365)
        return(self.edad)


nacimiento = datetime.datetime(1995, 12, 7)
yo = Persona(nacimiento)
print(str(yo.edad()) + " años.")
