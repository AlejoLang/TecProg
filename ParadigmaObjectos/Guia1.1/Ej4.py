peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / pow(altura, 2)

print("Resultado: ", imc)

if imc < 18.49:
  print("Peso bajo")
elif imc < 24.99:
  print("Peso normal")
elif imc < 29.99:
  print("Obesidad leve")
elif imc < 34.99:
  print("Obesidad media")
else:
  print("Obesidad morbida")