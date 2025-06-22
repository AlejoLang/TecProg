import datetime

class Persona:
  def __init__(self, nombre, edad, fecha_nacimiento):
    self.nombre = nombre
    self.edad = edad
    self.nacimiento = fecha_nacimiento

  def calcularEdad(self):
    dateToday = datetime.date.today()
    edad = dateToday - self.nacimiento
    return edad.days // 365
  
  def mostrar(self):
    cumpleaniosEsteAnio = datetime.date(datetime.date.today().year, self.nacimiento.month, self.nacimiento.day)
    print(self.nombre, ": ", self.calcularEdad(), "años ", cumpleaniosEsteAnio.strftime("%A")) 

if __name__ == "__main__":
  per = Persona("Juan", 32, datetime.date(2004,6,9))
  per.mostrar()