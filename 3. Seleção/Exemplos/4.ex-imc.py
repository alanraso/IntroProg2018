# Escreva um programa que recebe dois números como entrada: um
# peso (em kilogramas) e um altura (em metros) e imprime em que faixa do IMC
# a pessoa se enquadra:
#   + Até 18.5: desnutrido
#   + Entre 18.5 e 25: peso normal
#   + Entre 25 e 30: sobrepeso
#   + 30 ou mais: obesidade severa

def informa_imc(peso, altura):
  imc = peso / altura ** 2
  print(f'Seu IMC: {imc}')

  if imc < 18.5:
    print('Voce está subnutrido.')
  elif imc >= 18.5 and imc < 25:
    print('Voce esta no peso normal')
  elif imc >= 25 and imc < 30:
    print('Voce esta obeso')
  elif imc >= 30:
    print('Voce esta severamente obeso')

informa_imc(65, 1.70)
