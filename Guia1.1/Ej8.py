import math
radio = float(input("Introduce el radio de la base del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

areaCirculo = math.pi * pow(radio, 2)
volumen = areaCirculo * altura

print("Volumen: ", volumen)