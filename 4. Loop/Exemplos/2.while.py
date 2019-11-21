num = 1

while num < 100:
  print(num)
  num = num + 1

# Ou, na mesma linha:
num = 1
numeros = f'{num}'

while num < 100:
  print(num)
  num = num + 1
  numeros += f' {num}'

print(numeros)
