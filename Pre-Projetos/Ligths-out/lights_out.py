import lights_out_board as board

BOARD_SIZE = 5
YELLOW = '#F2B809'
WHITE = '#FFFFFF'

# TODO: tabuleiro válido aleatório de tamanho BOARD_SIZE
lights = [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1]

def toggleState(n):
    lights[n] = 1 if (lights[n] == 0) else 0

def get_color(n):
    return YELLOW if(lights[n] == 1) else WHITE

def toggle(n):
    toggleState(n)
    board.paint_circle(n, get_color(n))

def initial_fill():
    for i in range(0, 25):
        board.paint_circle(i, get_color(i))

def adjascents(n):
    adjascents = []

    if (n >= BOARD_SIZE):
        adjascents.append(n - BOARD_SIZE)
    if (n % BOARD_SIZE != 0):
        adjascents.append(n - 1)
    if (n % BOARD_SIZE != BOARD_SIZE - 1):
        adjascents.append(n + 1)
    if (n < BOARD_SIZE**2 - BOARD_SIZE):
        adjascents.append(n + BOARD_SIZE)

    return adjascents

def toggle_clicked_and_adjascents(n):
    lights_to_toggle = adjascents(n)
    lights_to_toggle.append(n)
    for i in lights_to_toggle:
        toggle(i)

def main():
    board.draw_board(BOARD_SIZE, WHITE)
    initial_fill()
    board.register_click(toggle_clicked_and_adjascents)
    board.end()

if __name__ == "__main__":
    main()
