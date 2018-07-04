# Calcula IMC e dá o parecer

def calcula_imc():
  peso = float(input('Entre com seu peso (kg): '))
  altura = float(input('Entre com sua altura (m): '))

  imc = peso/altura**2

  mensagem = 'Seu IMC é ' + str(imc) + '\n'
  mensagem += 'Voce é considerado: '

  if imc < 17:
    mensagem += 'muito abaixo do peso'
  elif imc < 18.5:
    mensagem += 'abaixo do peso'
  elif imc < 25:
    mensagem += 'peso normal'
  elif imc < 30:
    mensagem += 'obeso'
  else:
    mensagem += 'muito obeso'
  
  print(mensagem)

termina = False

while not termina:
  calcula_imc()
  resposta = input('Calcular novamente? (s/n): ')
  print('') # Pular linha
  if resposta == 'S' or resposta == 's':
    termina = True
