from turtle import Turtle, Screen
from paddles import Paddles
from constants import WIDTH, HEIGHT, SCREEN_COLOR, STEP_ZISE

#Creando pantalla:  

screen = Screen()
screen.setup(width=WIDTH , height= HEIGHT) 
screen.bgcolor(SCREEN_COLOR)
screen.title("Mi Pong")


#Creamos y ubicamos los paddles:

player_1 = Paddles()
player_1.placement(w = WIDTH, place= "I")

player_2 = Paddles()
player_2.placement(w= WIDTH, place= "D")


# player_1.paddle.forward(STEPS)
# player_2.paddle.backward(STEPS)

player_1.up(1)

screen.exitonclick()
