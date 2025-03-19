segundos = int(input("Introduce el número de segundos: "))
horas = round(segundos / 3600)
minutos = round((segundos % 3600) / 60)
segundos = round((segundos % 3600) % 60)

print(horas, ":", minutos, ":", segundos)