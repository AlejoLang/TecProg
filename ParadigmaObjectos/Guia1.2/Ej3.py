N = int(input("¿Cuántos números deseas promediar? "))
suma = 0

for i in range(N):
  num = int(input(f"Num {i+1}: "))
  suma += num

print("Promedio: ", suma / N)