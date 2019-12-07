lista = []
num = int(input('Digite um número: '))

while num != -2:
  if num == -1:
    lista.clear()
  else:
    lista.append(num)
  print(lista)
  num = int(input('Digite um número: '))
