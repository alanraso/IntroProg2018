# -------
# Range
# -------

# De 0 a 4
numeros = ''
for i in range(5):
  numeros += f'{i} '
print(numeros)

# De 3 a 9
numeros = ''
for i in range(3, 9):
  numeros += f'{i} '
print(numeros)

# De 4 a 16, pulando (step) de 4 em 4
numeros = ''
for i in range(4, 16, 4):
  numeros += f'{i} '
print(numeros)

# -------
# String
# -------

for c in 'abacate':
  print(c)