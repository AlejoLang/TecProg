class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  def __str__(self):
    print(self.nombre, "tiene", self.edad, "años")

class Principal:
  def __init__(self):
    pass
  def ejecutar(self):
    persona1 = Persona("Pepe", 31)
    persona2 = Persona("Pepe", 31)

    print("Identidad de persona1: ", id(persona1))
    print("Identidad de persona2: ", id(persona2))
    if(persona1 is persona2):
      print("Iguales")
    else:
      print("Distintos")
    if(persona1.edad == persona2.edad and persona1.nombre == persona2.nombre):
      print("Iguales")
    else:
      print("Distintos")

if __name__ == "__main__":
  principal = Principal()
  principal.ejecutar()
  per = Persona("Pepe", 14)
  per.__str__()