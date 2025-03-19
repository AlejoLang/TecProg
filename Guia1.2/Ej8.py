import math
N = int(input("Introduce un número entero N para convertirlo a binario: "))
binario = ""

while N > 1:
  binario = str(N%2) + binario
  N = math.floor(N/2)
if N == 1:
  binario = "1" + binario
print(binario)