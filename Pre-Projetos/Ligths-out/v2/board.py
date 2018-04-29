import turtle
import board_aux as aux

my_t = turtle.Turtle()
aux.init(my_t)

def muda_cor_fundo(cor):
  my_t.getscreen().bgcolor(cor)

def desenha_circulo(pos_centro, raio, cor = '#FFFFFF'):
  aux.muda_pos(pos_centro)
  my_t.dot(2 * raio, cor)

def registrar_click(acao_click):
  my_t.getscreen().onclick(lambda x, y: acao_click((x, y)))

def end():
  turtle.done()