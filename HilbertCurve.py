from turtle import *

screen = Screen()
WIDTH,HEIGHT = screen.window_width(),screen.window_height()
size = 10
offset = 10

hideturtle()
penup()
goto(-WIDTH/2 + offset, HEIGHT/2 - offset)
pendown()

speed(300)

def hilbert(level, angle):
    if level == 0:
        return
    right(angle)
    hilbert(level - 1, -angle)
    forward(size)
    left(angle)
    hilbert(level - 1, angle)
    forward(size)
    hilbert(level - 1, angle)
    left(angle)
    forward(size)
    hilbert(level - 1, -angle)
    right(angle)

hilbert(6, 90)