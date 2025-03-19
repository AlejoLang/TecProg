N = int(input("¿Cuántos números vas a introducir? "))
max = -99999999
for i in range(N):
  num = int(input(f"Num {i+1}: "))
  if max < num: max = num

print(max)