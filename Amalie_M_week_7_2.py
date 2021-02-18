# Implement a Random Walker using Turtle Graphics

from turtle import Turtle
from random import choice

t = Turtle()
t.hideturtle()
t.pensize(6)
t.speed(7)
directions = [0, 90, 180, 270] #angles turtle can rotate

i = 0
while i < 200:    
    t.setheading(choice(directions)) #direction of turtle - default right, if 90 then up
    t.forward(20)
    i += 1



