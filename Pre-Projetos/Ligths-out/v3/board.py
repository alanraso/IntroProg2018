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
  my_t.getscreen().onclick(acao_click)
  
def input_popup(titulo, mensagem):
  return my_t.getscreen().textinput(titulo, mensagem)

def input_num_popup(titulo, mensagem, valor_min, valor_max):
  return my_t.getscreen().numinput(titulo, mensagem, 5, valor_min, valor_max)

def aguarda():
  turtle.done()

def limpa_tela():
  my_t.clear()

def fechar_janela():
  my_t.getscreen().bye()