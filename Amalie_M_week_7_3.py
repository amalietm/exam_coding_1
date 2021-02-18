# Bonus: Draw a Spirograph (using repeated basic shapes) or your Self-portrait using Turtle Graphics

import turtle
  
turtle.bgcolor('black') 
turtle.pensize(2) 
turtle.speed(30) 
  
# How many times drawn 
for i in range(6): 
    
    #color combination 
    for color in ('red', 'magenta', 'blue',  
                  'cyan', 'green', 'white', 
                  'yellow'): 
        turtle.color(color) 
          
        # Choosen size 
        turtle.circle(100) 
          
        # Move x pixels left to draw another circle 
        turtle.left(10) 
