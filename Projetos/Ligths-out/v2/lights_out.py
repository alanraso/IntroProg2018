import board

ACESO = '#FFFF00'
APAGADO = '#FFFFFF'

RAIO = 30
XC_INICIAL = -170
YC_INICIAL = 170
NAO_ACHOU = -10

estado = []
centros = []

def inicia_jogo():
  global estado
  estado = [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1]
  desenha_tabuleiro()
  board.registrar_click(faz_acao_clique)
  board.aguarda()

def desenha_tabuleiro():
  global centros
  xc = XC_INICIAL
  yc = YC_INICIAL
  desenha_circulo((xc, yc), 0)

  for i in range(1, 25):
    xc = xc + 2*RAIO + 5
    if i % 5 == 0:
      xc = XC_INICIAL
      yc = yc - (2*RAIO + 5)
    desenha_circulo((xc, yc), i)

def desenha_circulo(pos_centro, i):
  global centros
  cor = APAGADO if estado[i] == 0 else ACESO
  centros.append(pos_centro)
  board.desenha_circulo(pos_centro, RAIO, cor)

def faz_acao_clique(x, y):
  i = acha_indice_circ(x, y)
  if i == NAO_ACHOU: return
  pinta_adjascentes(i)
  if ganhou():
    mostra_mensagem_final()

def acha_indice_circ(x, y):
  for i in range(0, 25):
    xc = centros[i][0]
    yc = centros[i][1]
    if (x - xc)**2 + (y - yc)**2 <= RAIO**2:
      return i
  return NAO_ACHOU

def pinta_adjascentes(i):
  indices_para_pintar = acha_i_adjascentes(i) + (i,)
  for j in indices_para_pintar:
    troca_estado_circulo(j)

def acha_i_adjascentes(i):
  if i == 0: return (1, 5)
  elif i == 4: return (3, 9)
  elif i == 20: return (15, 21)
  elif i == 24: return (19, 23)
  elif i < 4: return (i-1, i+1, i+5) # Primeira linha
  elif i > 20: return (i-5, i-1, i+1) # Última linha
  elif i % 5 == 0: return (i-5, i+1, i+5) # Primeira coluna
  elif i % 5 == 4: return (i-5, i-1, i+5) # Última coluna
  else: return (i-5, i-1, i+1, i+5)

def troca_estado_circulo(i):
  estado[i] = not estado[i]
  cor = APAGADO if estado[i] == 0 else ACESO
  board.pinta_circulo(centros[i], RAIO, cor)

def ganhou():
  primeira = estado[0]
  for e in estado:
    if e != primeira: return False
  return True

def mostra_mensagem_final():
  resposta = board.input_popup('GANHOOOOOU!', 'Deseja jogar novamente? (s/n)')
  if resposta == 's' or resposta == 'S':
    inicia_jogo()
  else:
    board.fechar_janela()

def main():
  board.titulo('Lights-out')
  board.muda_cor_fundo('#222222')
  inicia_jogo()

if __name__ == "__main__":
  main()