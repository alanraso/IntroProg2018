import board

MENSAGEM_INICIAL = 'O objetivo deste jogo é apagar todas as lâmpadas, ou ascender todas.\nQual seu nome?'

def verifica_circulo(x, y):
  print(x, y)

def desenha_tabuleiro():
  board.desenha_circulo([0, 0], 30, '#FF0000')

def main():
  board.titulo('Lights-out')
  desenha_tabuleiro()
  nome = board.input_popup('Bem-vindo ao Lights-out!', MENSAGEM_INICIAL)
  board.registrar_click(verifica_circulo)
  print(nome)
  board.aguarda()

if __name__ == "__main__":
  main()