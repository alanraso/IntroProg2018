n = int(input('Entre com o número inteiro: '))
num_aux = n
contador = 0

while num_aux != 0:
  num_aux = num_aux//10
  contador += 1

print('O numero de algarismos do numero', n, 'eh', contador)