def calcula_imc():
  peso = float(input('Digite seu peso em kg: '))
  altura = float(input('Digite sua altura em m: '))
  imc = peso / altura ** 2

  if imc < 18.5:
    faixa = 'abaixo do peso'
  elif imc >= 18.5 and imc < 25:
    faixa = 'peso normal'
  elif imc >= 25 and imc < 30:
    faixa = 'sobrepeso'
  elif imc >= 30 and imc < 35:
    faixa = 'obeso'
  
  print(f'Seu imc é {imc}. Você é classificado como {faixa}')

continua_calculando = True
while continua_calculando:
  calcula_imc()
  resposta = input('Deseja realizar outra medida? (S/N) ')
  if resposta != 'S' and resposta != 's':
    continua_calculando = False
  print('') # Apenas para pular linha
