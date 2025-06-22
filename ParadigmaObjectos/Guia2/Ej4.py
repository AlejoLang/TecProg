import hashlib
import datetime
import encodings

class Persona:
  def __init__(self, nombre, edad, fecha_nacimiento, password):
    self.nombre = nombre
    self.edad = edad
    self.nacimiento = fecha_nacimiento
    self.password = hashlib.sha256(password.encode())

  def calcularEdad(self):
    dateToday = datetime.date.today()
    edad = dateToday - self.nacimiento
    return edad.days // 365

  def validatePassword(self, password):
    return hashlib.sha256(password.encode()).hexdigest() == self.password.hexdigest()
  
  def mostrar(self):
    cumpleaniosEsteAnio = datetime.date(datetime.date.today().year, self.nacimiento.month, self.nacimiento.day)
    print(self.nombre, ": ", self.calcularEdad(), "años ", cumpleaniosEsteAnio.strftime("%A")) 

if __name__ == "__main__":
  per = Persona("Juan", 32, datetime.date(2004,6,9), "asdfasdfasdfasdfasdfasdfasdfsdfasdf")
  per.mostrar()
  val = per.validatePassword("asdfasdfasdfasdfasdfasdfasdfsdfasdf")
  print(val)