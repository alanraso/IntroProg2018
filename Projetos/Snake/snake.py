import time
from datetime import datetime
from random import randint
from window import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, WIN_Y, WIN_X, run

# Constants
NO_WALL = True
SCORE_POSITION = [0, 2]
TITLE_POSITION = [0, 27]
ESC_KEY = 27
PAUSE_KEY = 32
FOOD_CHAR = '*'
SNAKE_CHAR = '#'
DIR_KEYS = [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN]
KNOWN_KEYS = [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, ESC_KEY, PAUSE_KEY]

# State control variables
snake = [[4, 10], [4, 9], [4, 8]]
food = []
score = 0
paused = False

def show_board_header(win):
  win.addstr(*SCORE_POSITION, "Score : {}".format(score))
  win.addstr(*TITLE_POSITION, ' SNAKE ')

def update_snake_speed(win):
  win.timeout(150 - (int(len(snake) / 5) + int(len(snake) / 10)) % 120)

def pause_game(win):
  while True:
    if win.getch() == PAUSE_KEY:
      break
      
def check_boundaries(mode=NO_WALL):
  if mode == NO_WALL:
    if snake[0][0] == 0: snake[0][0] = WIN_Y - 2
    if snake[0][1] == 0: snake[0][1] = WIN_X - 2
    if snake[0][0] == WIN_Y - 1: snake[0][0] = 1
    if snake[0][1] == WIN_X - 1: snake[0][1] = 1

    return True
  else:
    if snake[0][0] == 0 or snake[0][0] == WIN_Y - 1 or snake[0][1] == 0 or snake[0][1] == WIN_X - 1:
      return False

    return True

def snake_suicide():
  return snake[0] in snake[1:]

def change_food_position(win):
  global food

  food = []
  while food == []:
    food = [randint(1, 18), randint(1, 58)]
    if food in snake: food = []
  win.addch(food[0], food[1], FOOD_CHAR) 

def inc_score():
  global score
  score += 1

def found_food(win):
  if snake[0] == food:
    inc_score()
    change_food_position(win)
    return True

  return False

def update_snake_size(win, key):
  snake.insert(
    0, [
      snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), 
      snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)
    ])
  break_conditions = [not check_boundaries(), snake_suicide()]

  if True in break_conditions:
    return False

  if not found_food(win):
    last = snake.pop()
    win.addch(last[0], last[1], ' ')

  win.addch(snake[0][0], snake[0][1], SNAKE_CHAR)

  return True

def determine_keys(win, curr_key):
  event = win.getch()

  if event in KNOWN_KEYS:
    return [curr_key, event]

  return [curr_key, curr_key]

def main(win):
  change_food_position(win)
  prev_key = curr_key = KEY_RIGHT

  while curr_key != ESC_KEY:
    show_board_header(win)
    update_snake_speed(win)

    prev_key, curr_key = determine_keys(win, curr_key)

    if curr_key == PAUSE_KEY:
      pause_game(win)
      curr_key = prev_key
      continue

    if update_snake_size(win, curr_key) == False:
      break

if __name__ == '__main__':
  run(main)