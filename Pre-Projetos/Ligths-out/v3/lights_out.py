# -*- coding: utf-8 -*-
import board

RAIO = 25
DIST = 5

MENSAGEM_INICIAL = 'O objetivo deste jogo é apagar todas as lâmpadas, ou ascender todas.\nQual dimensao do seu jogo?'

def desenha_circulo(x, y,aceso):
  color = '#FFFF00' if aceso else '#000000'
  board.desenha_circulo([INICIO+(2*x+1)*(RAIO+DIST), INICIO+(2*y+1)*(RAIO+DIST)], RAIO, color)

def desenha_tabuleiro(dim):
  for i in list(range(dim)):
    desenha_circulo(i,i, False)
    for j in list(range(i+1, dim)):
      desenha_circulo(i,j, False)
      desenha_circulo(j,i, False)

def main():
  board.titulo('Lights-out')
  board.muda_cor_fundo('#ffffff')
  dim = int(board.input_num_popup('Bem vindo!!', MENSAGEM_INICIAL, 3, 10))
  total = dim*(2*RAIO) + ((dim+1)*DIST)
  global INICIO 
  INICIO = -(total-1)/2
  desenha_tabuleiro(dim)
  board.aguarda()

if __name__ == "__main__":
  main()

