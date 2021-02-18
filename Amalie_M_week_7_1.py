import turtle

t = turtle.Turtle()

sides = int(input("how many sides do you want your polygon to have: "))
side_length = int(input("what are the lengths of the sides of your polygon: "))

def polygon(side_length, sides):
    for i in range(0, sides):
        t.forward(side_length)
        t.right(360 / sides)

    turtle.done()
    
polygon(side_length, sides)
