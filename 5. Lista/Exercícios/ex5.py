import random

lista = []

for i in range(0, 19):
  lista.append(random.randint(1, 100))

print(lista)

maior = 0
for num in lista:
  if num > maior:
    maior = num

print(maior)
