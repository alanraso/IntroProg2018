# -*- coding: utf-8 -*-
import board

RAIO = 40
DISTANCIA_ENTRE_LAMPADAS = 5
DIMENSAO = 5
COR_FUNDO = '#FFFFFF'
COR_ACESO = '#FFFF00'
COR_APAGADO = '#000000'
CENTROS = []
ESTADOS_LAMPADAS = []
ESTADO_INICIAL_LAMPADAS = [
  [False, True, False, False, True],
  [True, False, False, True, False],
  [False, False, False, True, False],
  [True, True, True, True, False],
  [True, False, True, False, False],
]

def acha_circulo(x, y):
  for i in range(DIMENSAO):
    for j in range(DIMENSAO):
      centro_x = CENTROS[i][j][0]
      centro_y = CENTROS[i][j][1]
      if (x - centro_x) ** 2 + (y - centro_y) ** 2 <= RAIO ** 2:
        return (i, j)

  return None

def desenha_circulo(pos, aceso):
  color = COR_ACESO if aceso else COR_APAGADO
  board.desenha_circulo(pos, RAIO, color)

def desenha_tabuleiro():
  for i in range(DIMENSAO):
    CENTROS.append([])
    ESTADOS_LAMPADAS.append([])
    for j in range(DIMENSAO):
      centro_x = i * (2 * RAIO + DISTANCIA_ENTRE_LAMPADAS)
      centro_y = j * (2 * RAIO + DISTANCIA_ENTRE_LAMPADAS)
      CENTROS[i].append((centro_x, centro_y))
      ESTADOS_LAMPADAS[i].append(ESTADO_INICIAL_LAMPADAS[i][j])
      desenha_circulo((centro_x, centro_y), ESTADOS_LAMPADAS[i][j])

def atualiza(i, j):
  ESTADOS_LAMPADAS[i][j] = 0 if ESTADOS_LAMPADAS[i][j] == 1 else 1
  desenha_circulo(CENTROS[i][j], ESTADOS_LAMPADAS[i][j])

def clicar(x, y):
  c = acha_circulo(x, y)

  if c == None:
    return

  atualiza(c[0], c[1])

  if c[0] + 1 < DIMENSAO:
    atualiza(c[0]+1, c[1])
  if c[1] + 1 < DIMENSAO:
    atualiza(c[0], c[1]+1)
  if c[0] - 1 >= 0:
    atualiza(c[0]-1, c[1])
  if c[1] - 1 >= 0:
    atualiza(c[0], c[1]-1)
  if venceu():
    finaliza_jogo()

def venceu():
  a = ESTADOS_LAMPADAS[0][0]

  for i in range(DIMENSAO):
    for j in range(DIMENSAO):
      if ESTADOS_LAMPADAS[i][j] != a:
        return False

  return True

def finaliza_jogo():
  res = board.input_popup("Parabens", "Você ganhou o jogo! Deseja jogar novamente? (S / N)")

  if res == 'S' or res == 's':
    inicio_jogo()
  else:
    board.fechar_janela()

def inicio_jogo():
  CENTROS.clear()
  board.limpa_tela()
  desenha_tabuleiro()
  board.registrar_click(clicar)
  board.aguarda()

def main():
  board.titulo('Lights-out')
  board.muda_cor_fundo(COR_FUNDO)
  inicio_jogo()

if __name__ == "__main__":
  main()
