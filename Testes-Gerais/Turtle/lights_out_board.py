import turtle

RADIUS = 50
my_t = turtle.Turtle()

def skip_animations():
    my_t.speed(0)
    my_t._tracer(0, 0)

def initial_setup():
    skip_animations()
    my_t.getscreen().bgcolor('#222222')
    my_t.pen(my_t.pen(), shown=False) # Hide Pen
    set_pos_to_initial()
    my_t.pencolor('#222222')

def set_pos_to_initial():
    my_t.penup()
    my_t.setpos(-200, 200) # Gambiarra pro top-left
    my_t.pendown()

def draw_circle(fill_color = '#FFFFFF'):
    my_t.fillcolor(fill_color)
    my_t.begin_fill()
    my_t.circle(RADIUS)
    my_t.end_fill()

def draw_horizontal_circles(quantity, fill_color = '#FFFFFF'):
    for i in range(0, quantity):
        draw_circle(fill_color)
        my_t.penup()
        my_t.forward(2*RADIUS)
        my_t.pendown()

def draw_board(n, fill_color = '#FFFFFF'):
    for i in range(0, n):
        draw_horizontal_circles(n, fill_color)
        set_pos_to_initial()
        my_t.penup()
        my_t.setheading(270)
        my_t.forward(2*(i+1)*RADIUS)
        my_t.setheading(0)
        my_t.pendown()


initial_setup()
draw_board(5)

turtle.done()
