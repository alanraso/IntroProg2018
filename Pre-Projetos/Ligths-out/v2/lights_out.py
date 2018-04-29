import board

def quando_clicka(pos):
  print(pos[0], pos[1])
  board.desenha_circulo([0, 0], 50, '#FF0000')

def main():
  board.registrar_click(quando_clicka)
  board.desenha_circulo([0, 0], 50)
  board.end()

if __name__ == "__main__":
  main()