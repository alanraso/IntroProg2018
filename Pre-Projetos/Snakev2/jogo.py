import random

import cobra_engine
from cobra_engine import TAMANHO_HORIZONTAL, TAMANHO_VERTICAL

PAREDES_LETAIS = False
cobra = [[10, 10], [10, 11], [10, 12], [10, 13]]

def move_comida():
  global comida
  comida = coordenadas_comida()

def coordenadas_comida():
  # Projeto
  posicao_horizon = random.randint(0, TAMANHO_HORIZONTAL - 1)
  posicao_vertical = random.randint(0, TAMANHO_VERTICAL - 1)

  if [posicao_vertical, posicao_horizon] in cobra:
    return coordenadas_comida()
  else:
    return [posicao_vertical, posicao_horizon]

def mostrar_tabuleiro(cobra):
  # Projeto
  representacao = '-' * (TAMANHO_HORIZONTAL + 2) + '\n'

  for i in range(TAMANHO_VERTICAL):
    representacao += '|'
    for j in range(TAMANHO_HORIZONTAL):
      if [i, j] in cobra:
        representacao += '#'
      elif [i, j] == comida:
        representacao += '*'
      else:
        representacao += ' '
    representacao += '|\n'

  representacao += '-' * (TAMANHO_HORIZONTAL + 2) + '\n'

  cobra_engine.limpa_tela()
  print(representacao)

def move_cobra(direcao, proxima_direcao):
  # Projeto
  cabeca = cobra[0]
  corpo = cobra[1:]
  posicao_anterior = [cabeca[0], cabeca[1]]

  ultima_posicao_corpo = corpo[-1]

  if proxima_direcao == 'ESQUERDA':
      cabeca[1] -= 1
  elif proxima_direcao == 'DIREITA':
      cabeca[1] += 1
  elif proxima_direcao == 'ABAIXO':
      cabeca[0] += 1
  elif proxima_direcao == 'ACIMA':
      cabeca[0] -= 1
  
  if cabeca == comida:
    corpo = corpo + [ultima_posicao_corpo]
  elif cabeca in corpo:  
    cobra_engine.finalizar_jogo('Cobra se matou. Pontuacao final: ', len(cobra) - 4)

  for i in range(len(corpo)):
    tmp = corpo[i]
    corpo[i] = posicao_anterior
    posicao_anterior = tmp

  if PAREDES_LETAIS:
    if cabeca[0] < 0 or cabeca[1] < 0 or cabeca[0] >= TAMANHO_VERTICAL or cabeca[1] >= TAMANHO_HORIZONTAL:
      cobra_engine.finalizar_jogo('Espatifou-se na parede. Pontuacao final: ', len(cobra) - 4)
  else:
    if cabeca[0] < 0 or cabeca[0] >= TAMANHO_VERTICAL:
      cabeca[0] = cabeca[0] % TAMANHO_VERTICAL
    elif cabeca[1] < 0 or cabeca[1] >= TAMANHO_HORIZONTAL:
      cabeca[1] = cabeca[1] % TAMANHO_HORIZONTAL

  return [cabeca] + corpo

comida = coordenadas_comida()

def loop(direcao, proxima_direcao):
  # Projeto
  global cobra
  nova_cobra = move_cobra(direcao, proxima_direcao)

  if len(nova_cobra) > len(cobra):
    cobra_engine.incrementa_pontuacao()
    move_comida()

  cobra = nova_cobra
  mostrar_tabuleiro(cobra)
  cobra_engine.atualiza(len(cobra))

if __name__ == '__main__':
  cobra_engine.rodar(loop)