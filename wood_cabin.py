# Importation modules 
from turtle import *

# Definition of the properties of the pencil
shape('turtle') # shape of the pointer, in this case a turtle
pensize(3) # line thickness
speed(2) # pointer speed
colormode(255) # return all colors
color(180, 70, 200) # line color
fillcolor("yellow") # pointer color

# Definition of facade
def Facade(Prating_square, square_x, square_y):
    up() # lift the pointer
    goto(square_x, square_y) # the pointer is placed at x and y coordinates
    setheading(0) # resets the pointer to 0
    down() # put the pointer down
    for i in range(4): # Draw four sides
        forward(Prating_square) # advance on each side of the square
        right(90) # 90 degrees to the right

# Definition of Roof
def Roof(Prating_square, square_x, square_y):
    up()
    goto(square_x, square_y)
    down()
    for i in range(3): # Draw three sides
        forward(Prating_square)
        left(120)

# Definition of Door
def Door(Prating_square, square_x, square_y):
    up()
    goto(square_x, square_y)
    setheading(0) # resets the pointer to 0
    down()
    for i in range(2): # Draw two sides
        forward(Prating_square / 2)
        left(90)
        forward(Prating_square)
        left(90)

# Definition of Window
def Window(P_ray, square_x, square_y):
    up()
    goto(square_x, square_y)
    setheading(0) # resets the pointer to 0
    down()
    circle(P_ray) # draws the circle according to the defined radius

# Construction of the hut
def Hut(Prating_square, square_x, square_y):
    Facade(Prating_square, square_x, square_y)
    Roof(Prating_square * 1.5, square_x + Prating_square * -0.25, square_y)
    Door(Prating_square / 2, square_x + Prating_square * 0.60, square_y - Prating_square)
    Window(Prating_square / 6, square_x + Prating_square * 0.30, square_y + Prating_square * -0.50)

# We call the cabin
Hut(100, 0, 150)
Hut(50, 140, 150)