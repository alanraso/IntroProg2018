import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, wrapper

WIN_Y = 20
WIN_X = 60
WINDOW_DIMENSIONS = [WIN_Y, WIN_X, 0, 0]

curses_initialized = False

def init_curses():
  global curses_initialized

  if curses_initialized == True:
    return False

  curses.initscr()
  curses.noecho()
  curses.curs_set(0)
  curses_initialized = True

def create_window():
  global curses_initialized

  if curses_initialized == False:
    init_curses()

  win = curses.newwin(*WINDOW_DIMENSIONS)
  win.keypad(True) # Escape sequences will be interpreted by curses
  win.border(0) # Use default characters for borders
  win.nodelay(True) # make `getch` non-blocking 

  return win

def run(func):
  return func(create_window())