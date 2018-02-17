import turtle

screen = turtle.Turtle()
screen.speed(0)
screen.pen(screen.pen(), shown=False)

screen.color('#000000')
screen.begin_fill()
screen.circle(50)
screen.end_fill()

turtle.done()