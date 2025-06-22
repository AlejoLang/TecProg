import datetime

class Inscripcion:
  def __init__(self, alumno, carrera, fechaInsc):
    self.fechaInscripcion = fechaInsc
    self.alumno = alumno
    self.carrera = carrera
  def getAlumno(self): return self.alumno
  def getCarrera(self): return self.carrera
  def getFecha(self): return self.fechaInscripcion

class Alumno:
  def __init__(self, nombre, dni, nac):
    self.nombre = nombre
    self.dni = dni
    self.fechaNacimiento = nac
  def calcularEdad(self):
    dateToday = datetime.date.today()
    edad = dateToday - self.nacimiento
    return edad.days // 365

class Carrera:
  def __init__(self, nombre):
    self.nombre = nombre

class Facultad:
  def __init__(self, nombre):
    self.nombre = nombre
    self.carreras = []
  def addCarrera(self, carrera):
    self.carreras.append(carrera)
  def mostrarCarrerasYAlumnos(self):
    print("Facultad: ", self.nombre)
    for carrera in self.carreras:
      print("Carrera: ", carrera)
      print("Alumnos:")
      for inscripcion in carrera.getInscripciones():
        print(" - ", inscripcion.getAlumno().nombre, " - ", inscripcion.getFecha())

inscripciones = []

