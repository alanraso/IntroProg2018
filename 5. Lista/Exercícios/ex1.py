lista = [2, 20, 7, 45, 99, 101, 62, -3, 66]

def troca(i1, i2):
  temp = lista[i1]
  lista[i1] = lista[i2]
  lista[i2] = temp

troca(3, 5)

print(lista)
