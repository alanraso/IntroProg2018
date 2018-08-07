# E se eu quiser imprimir todos os quadrados de 0 a n?

n = int(input('Digite n: '))
i = 0

while i <= n:
  print(i**2)
  i = i + 1

# Usando 'for'

print('')

for i in range(0, n+1):
  print(i**2)