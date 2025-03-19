N = int(input("Introduce un número entero N: "))
cont = 0
while N >= 1:
  cont += 1
  N /= 10

print(cont)