from math import *
from turtle import *

reset()
speed(10)

bgcolor("black")
color("white")

# this is a comment

for i in range(4):
    forward(100)
    left(90)

# circle

t = 0

while t < 2*pi:
    x = 100*cos(t)
    y = 100*sin(t)
    goto(x, y)
    t += .1

# rose curve

t = 0
width(5)
color("blue")

while t < pi:
    r = 100 * sin(3*t)
    x = r*cos(t)
    y = r*sin(t)
    goto(x, y)
    t += .01

# limacon

t = 0
color("yellow")

while t < 2*pi:
    r = 100 - 300*sin(t)
    x = r*cos(t)
    y = r*sin(t)
    goto(x,y)
    t += .1

# spiral

t = 0
color("green")
width(7)

while t < 12*pi:
    r = 10*t
    x = r*cos(t)
    y = r*sin(t)
    goto(x,y)
    t += .1
