import board

RAIO = 30
ACESO = '#FFFF00'
APAGADO = '#FFFFFF'
estado = [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1]
centros = []

def verifica_circulo(x, y):
  print(x, y)

def desenha_tabuleiro():
  global centros
  xc_inicial = -170
  yc_inicial = 170
  xc = xc_inicial
  yc = yc_inicial
  cor = APAGADO if estado[0] == 0 else ACESO
  centros.append([xc, yc])
  board.desenha_circulo([xc, yc], RAIO, cor)
  for i in range(1, 25):
    xc = xc + 2*RAIO + 5
    if i % 5 == 0:
      xc = xc_inicial
      yc = yc - (2*RAIO + 5)
    cor = APAGADO if estado[i] == 0 else ACESO
    centros.append([xc, yc])
    board.desenha_circulo([xc, yc], RAIO, cor)

def main():
  board.titulo('Lights-out')
  board.muda_cor_fundo('#222222')
  desenha_tabuleiro()
  board.registrar_click(verifica_circulo)
  board.aguarda()

if __name__ == "__main__":
  main()