import math
numero = float(input("Introduce un número (negativo para terminar): "))

while numero >= 0:
  print(math.sqrt(numero))
  numero = float(input("Introduce un número (negativo para terminar): "))