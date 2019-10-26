import math

def calcula_hipotenusa(cat1, cat2):
  hip_quadrado = cat1 ** 2 + cat2 ** 2
  return math.sqrt(hip_quadrado)

print(calcula_hipotenusa(3, 4)) # 5
print(calcula_hipotenusa(8, 15)) # 17
