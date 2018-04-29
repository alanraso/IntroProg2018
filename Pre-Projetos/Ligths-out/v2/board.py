import turtle
import board_aux as aux
import sys

my_t = turtle.Turtle()
aux.init(my_t)

def titulo(t):
  my_t.getscreen().title(t)

def muda_cor_fundo(cor):
  my_t.getscreen().bgcolor(cor)

def desenha_circulo(pos_centro, raio, cor = '#FFFFFF'):
  aux.muda_pos(pos_centro)
  my_t.dot(2 * raio, cor)

def registrar_click(acao_click):
  my_t.getscreen().onclick(lambda x, y: acao_click((x, y)))
  
def input_popup(titulo, mensagem):
  return my_t.getscreen().textinput(titulo, mensagem)

def aguarda():
  turtle.done()