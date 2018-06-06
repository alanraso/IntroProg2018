import turtle

CINZA = '#4A4A4A'

my_t = None

def init(turtle_var):
  global my_t
  my_t = turtle_var
  setup_inicial()

def setup_inicial():
  pular_animacoes()
  my_t.getscreen().bgcolor(CINZA)

def pular_animacoes():
  my_t.speed(0)
  my_t._tracer(0, 0)

def muda_pos(pos):
  my_t.penup()
  my_t.setpos(pos)
  my_t.pendown()
