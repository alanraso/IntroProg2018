import random

def joga_adivinha():
  print('-------------------------------------------')
  print('Bem-vindo(a) ao jogo de adivinhar o número!')
  print('-------------------------------------------\n')
  num = random.randint(0, 20)
  acertou = False
  tentativas = 0

  while not acertou and tentativas < 6:
    tentativas += 1
    chute = int(input('Chute o numero: '))
    if chute == num:
      print('Parabéns! Você acertou!')
      acertou = True
    elif chute > num:
      print('ERRRROU! O numero é menor do que isso')
    else:
      print('ERRRROU! O numero é maior do que isso')
    print('')

  if not acertou and tentativas == 6:
    print('Você usou todas as 6 tentativas =(')
  else:
    print('Foram usadas', tentativas, 'tentativas')

termina = False

while not termina:
  joga_adivinha()
  resp = input('Deseja jogar novamente? (s/n): ')
  print('')
  if resp != 's' and resp != 'S':
    termina = True