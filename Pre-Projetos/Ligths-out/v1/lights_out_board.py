import turtle

RADIUS = 40
SPACE = 2
NOT_A_CIRCLE = -1
my_t = turtle.Turtle()

circle_centers = []

def set_bg_color(color):
    my_t.getscreen().bgcolor(color)

def _skip_animations():
    my_t.speed(0)
    my_t._tracer(0, 0)

def _initial_setup():
    _skip_animations()
    my_t.getscreen().bgcolor('#4A4A4A')
    my_t.pen(my_t.pen(), shown=False) # Hide Pen
    _set_pos_to_initial()

def _set_pos_to_initial():
    _set_pos(-200, 200) # Gambiarra pro top-left

def _set_pos(x, y):
    my_t.penup()
    my_t.setpos(x, y)
    my_t.pendown()

def _set_pos_cor(cor):
    my_t.penup()
    my_t.setpos(cor[0], cor[1])
    my_t.pendown()

def _draw_circle(fill_color = '#FFFFFF'):
    my_t.fillcolor(fill_color)
    my_t.begin_fill()
    my_t.circle(RADIUS)
    my_t.end_fill()
    circle_centers.append((my_t.xcor(), my_t.ycor() + RADIUS))

def _draw_horizontal_circles(quantity, fill_color = '#FFFFFF'):
    for i in range(0, quantity):
        _draw_circle(fill_color)
        my_t.penup()
        my_t.forward(2*RADIUS + SPACE)
        my_t.pendown()

def draw_board(size, fill_color = '#FFFFFF'):
    _initial_setup()
    for i in range(0, size):
        _draw_horizontal_circles(size, fill_color)
        _set_pos_to_initial()
        my_t.penup()
        my_t.setheading(270)
        my_t.forward(2*(i+1)*(RADIUS + SPACE))
        my_t.setheading(0)
        my_t.pendown()

def paint_circle(n_circle, color):
    _set_pos_cor(circle_centers[n_circle])
    my_t.dot(2*RADIUS, color)

def _transform_coor_n(x, y):
    for i, center in enumerate(circle_centers):
        if ((x - center[0])**2 + (y - center[1])**2 <= RADIUS**2):
            return i
    return NOT_A_CIRCLE

def register_click(onclick):
    my_t.getscreen().onclick(lambda x, y: onclick(_transform_coor_n(x, y)))

def write(text):
    my_t.color('#FFFFFF')
    _set_pos(-50, -250)
    my_t.write(text, False, 'center', ("Arial", 16, "bold"))

def open_dialog(title, text):
    return my_t.getscreen().textinput(title, text)

def end():
    turtle.done()

def main():
    draw_board(5)
    end()

if __name__ == "__main__":
    main()