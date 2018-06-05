from multiprocessing import Process, Manager, Value
from ctypes import c_char_p
import sys, time, os

TAMANHO_HORIZONTAL = 40
TAMANHO_VERTICAL = 20

pontuacao = 0
manager = Manager()
bloqueia_entrada = manager.Value(c_char_p, "0")
direcao = manager.Value(c_char_p, "ESQUERDA")
proxima_direcao = manager.Value(c_char_p, "ESQUERDA")

fn = sys.stdin.fileno()

def ler_entrada(direcao, proxima_direcao, bloqueia_entrada, fn):
  try:
    # Especifico para Windows
    import msvcrt
    return msvcrt.getch()

  except ImportError:
    import tty, sys, termios, os, time

    sys.stdin = os.fdopen(fn)
    termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    
    try:
      while True:
        ch = sys.stdin.read(3)
        if bloqueia_entrada.value == '0':
          if ch == '\x1b[A':
            if proxima_direcao.value != 'ABAIXO':
              direcao.value = proxima_direcao.value
              proxima_direcao.value = "ACIMA"
              bloqueia_entrada.value = '1'
          elif ch == '\x1b[B':
            if proxima_direcao.value != 'ACIMA':
              direcao.value = proxima_direcao.value
              proxima_direcao.value = "ABAIXO"
          elif ch == '\x1b[C':
            if proxima_direcao.value != 'ESQUERDA':
              direcao.value = proxima_direcao.value
              proxima_direcao.value = "DIREITA"
              bloqueia_entrada.value = '1'
          elif ch == '\x1b[D':
            if proxima_direcao.value != 'DIREITA':
              direcao.value = proxima_direcao.value
              proxima_direcao.value = "ESQUERDA"
              bloqueia_entrada.value = '1'
        elif bloqueia_entrada.value == '-1':
          sys.exit(1)
    finally:
      pass

def incrementa_pontuacao():
  global pontuacao
  pontuacao += 1

def atualiza(tamanho_cobra):
  atualiza_velocidade(calcula_velocidade(tamanho_cobra))

def calcula_velocidade(tamanho_cobra):
  if tamanho_cobra > 100:
    return 0.45

  # min = 0.9 max 0.04
  return (112 - 1.129 * (tamanho_cobra - 4)) / (TAMANHO_VERTICAL * TAMANHO_HORIZONTAL)

def atualiza_velocidade(tamanho_cobra):
  global velocidade
  velocidade = calcula_velocidade(tamanho_cobra)

def limpa_tela():
  os.system('cls' if os.name=='nt' else 'clear')

def finalizar_jogo(mensagem):
  print(mensagem, pontuacao)
  bloqueia_entrada.value = '-1'
  sys.exit(0)

def rodar(main):
  def processo_entradas():
    p = Process(target=ler_entrada, args=(direcao, proxima_direcao, bloqueia_entrada, fn))
    p.start()

    return p

  def processo_graficos():
    p = Process(target=loop_principal(main))
    p.start()

    return p

  for processo in [processo_graficos(), processo_entradas()]:
    processo.join()

def loop_principal(f):
  def wrapper(*args, **kwargs):
    velocidade = calcula_velocidade(0)
    while True:
      args = (direcao.value, proxima_direcao.value)
      f(*args, **kwargs)
      bloqueia_entrada.value = "0"
      time.sleep(velocidade)
  return wrapper