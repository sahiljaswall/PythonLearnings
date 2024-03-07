from turtle import *
from random import randint
def position_turtle(diff):
    penup()
    hideturtle()
    setposition(-250,-250+diff)
    showturtle()
    pendown()   
def move_turtle():
    penup()
    hideturtle()
    forward(25)
    showturtle()
    pendown()   


def random_colors():
    r=randint(100,255)
    g=randint(100,255)
    b=randint(100,255)
    return "#%02x%02x%02x" % (r, g, b)

difference=0
position_turtle(difference)
speed(10)
for _ in range(20):
    for _ in range(20):
        pencolor(random_colors())
        dot(10)
        move_turtle()
    difference+=25
    position_turtle(difference)
done()

