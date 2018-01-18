from graphics import *

def main():
    window = GraphWin("Lights Out", 250, 250)
    print("ALO1")
    draw_lines(window)
    print("ALO2")
    display_lights(window, [[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,1,0,1,0]])

def draw_lines(window):
    line1 = Line(Point(0,50),Point(250,50))
    line1.draw(window)  
    line2 = Line(Point(0,100),Point(250,100))
    line2.draw(window)
    line3 = Line(Point(0,150),Point(250,150))
    line3.draw(window)
    line4 = Line(Point(0,200),Point(250,200))
    line4.draw(window)
    line5 = Line(Point(50,0),Point(50,250))
    line5.draw(window)
    line6 = Line(Point(100,0),Point(100,250))
    line6.draw(window)
    line7 = Line(Point(150,0),Point(150,250))
    line7.draw(window)
    line8 = Line(Point(200,0),Point(200,250))
    line8.draw(window)

def display_lights(window,board):
        for row in range(5):
                for column in range(5):
                        center = Point(column*50+25,row*50+25)
                        circ = Circle(center,25)
                        if (board[row][column] == 1):
                                circ.setFill("yellow")
                        else:
                                circ.setFill("white")
                        circ.draw(window)

if __name__ == "__main__":
    main()