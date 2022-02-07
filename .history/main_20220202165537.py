from ast import While
from tkinter import Y
from turtle import Turtle, Screen
from paddles import Paddles
from ball import Ball
from constants import WIDTH, HEIGHT, SCREEN_COLOR, STEP_ZISE, ORIGIN
from math import pi, sin, cos 
import random 

# 0) variables:

#para la pelota. 
y_step = sin(45* pi/180) * STEP_ZISE
x_step = cos(45* pi/180) * STEP_ZISE

# I) Creando pantalla:  

screen = Screen()
screen.setup(width=WIDTH , height= HEIGHT) 
screen.bgcolor(SCREEN_COLOR)
screen.title("Mi Pong")


# II) Creamos y ubicamos los paddles:

player_1 = Paddles()
player_1.placement(w = WIDTH, place= "I")

player_2 = Paddles()
player_2.placement(w= WIDTH, place= "D")


# III) Mover paddles con las teclas:

screen.listen()

#Player 1:
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")

#Player 2:

screen.onkey(player_2.up, "Up")
screen.onkey(player_2.down, "Down")


# IV) Crear pelota en movimiento. 

#Pelota creada:

ball = Ball()

#mover pelota:

quadrants = [1,2,3,4] 
While True: 
    q = random.choice(quadrants) 
    ball.ball_movement(q)


# player_1.up(1)
# player_1.down(5)

screen.exitonclick()
