N = int(input("¿Cuántos números deseas sumar? "))
suma = 0

for i in range(N):
  num = int(input(f"Introduce el numero {i+1}: "))
  suma += num

print("Total: ", suma)