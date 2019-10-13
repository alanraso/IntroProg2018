# -*- coding: utf-8 -*-
import board

RAIO = 25
DIST = 5
COR_FUNDO = '#FFFFFF'
COR_ACESO = '#FFFF00'
COR_APAGADO = '#000000'

MENSAGEM_INICIAL = 'O objetivo deste jogo é apagar todas as lâmpadas, ou acender todas.\nQual dimensao do seu jogo?'

def centro_circulo(x,y):
  return [centro_circulo_uni(x), centro_circulo_uni(y)]

def centro_circulo_uni(x):
  return INICIO+(2*x+1)*(RAIO+DIST)

def achar_circulo(x, y):
  x_1 = achar_circulo_uni(x)
  y_1 = achar_circulo_uni(y)
  return [x_1 , y_1]

def achar_circulo_uni(x):
  for i in list(range(DIM)):
    if (x > (centro_circulo_uni(i) - RAIO) and x < (centro_circulo_uni(i) + RAIO)):
      return i

def desenha_circulo(x, y,aceso):
  color = COR_ACESO if aceso else COR_APAGADO
  board.desenha_circulo(centro_circulo(x, y), RAIO, color)

def desenha_tabuleiro():
  for i in list(range(DIM)):
    desenha_circulo(i,i, False)
    for j in list(range(i+1, DIM)):
      desenha_circulo(i,j, False)
      desenha_circulo(j,i, False)

def inicia_matrix():
  global MATRIX
  MATRIX = [0] * DIM
  for i in list(range(DIM)):
    MATRIX[i] = [0] * DIM

def atualiza_matrix(x, y):
  MATRIX[x][y] = 0 if MATRIX[x][y]==1 else 1

def atualiza(x, y):
  atualiza_matrix(x, y)
  desenha_circulo(x, y, MATRIX[x][y])

def clicar(x, y):
  c = achar_circulo(x, y)
  atualiza(c[0], c[1])
  if(c[0] + 1 < DIM):
    atualiza(c[0]+1, c[1])
  if(c[1] + 1 < DIM):
    atualiza(c[0], c[1]+1)
  if(c[0] - 1 >= 0):
    atualiza(c[0]-1, c[1])
  if(c[1] - 1 >= 0):
    atualiza(c[0], c[1]-1)
  if(venceu()):
    fim_jogo()

def venceu():
  a = MATRIX[0][0]
  for i in list(range(0,DIM)):
    if(MATRIX[i][i] != a): 
      return False
    for j in list(range(i+1,DIM)):
      if(MATRIX[i][j] != a or MATRIX[j][i]!=a): 
        return False
  return True

def fim_jogo():
  res = board.input_popup("Parabens", "Muito bem!!Você ganhou o jogo =D =D\nDigite 'sim' para jogar novamente.")
  if(res == 'sim'):
    inicio_jogo()
  else:
    board.fechar_janela()

def inicio_jogo():
  board.limpa_tela()
  global DIM
  DIM = int(board.input_num_popup('Bem vindo!!', MENSAGEM_INICIAL, 3, 10))
  total = DIM*(2*RAIO) + ((DIM+1)*DIST)
  global INICIO 
  INICIO = -(total)/2
  desenha_tabuleiro()
  inicia_matrix()
  board.registrar_click(clicar)
  board.aguarda()

def main():
  board.titulo('Lights-out')
  board.muda_cor_fundo(COR_FUNDO)
  inicio_jogo()

if __name__ == "__main__":
  main()
