import board

MENSAGEM_INICIAL = 'O objetivo deste jogo é apagar todas as lâmpadas, ou ascender todas.\nQual seu nome?'

def quando_clicka(pos):
  print(pos[0], pos[1])

def desenha_tabuleiro():
  board.desenha_circulo([0, 0], 50, '#FF0000')

def main():
  board.titulo('Lights-out')
  desenha_tabuleiro()
  nome = board.input_popup('Bem-vindo ao Lights-out!', MENSAGEM_INICIAL)
  board.registrar_click(quando_clicka)
  print(nome)
  board.aguarda()

if __name__ == "__main__":
  main()