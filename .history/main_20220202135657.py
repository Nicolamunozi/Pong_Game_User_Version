from turtle import Turtle, Screen
from paddles import Paddles

#CONSTANTES:

WIDTH =  800
HEIGHT =  800
SCREEN_COLOR =  "black" 
STEPS = 20

#Creando pantalla:  

screen = Screen()
screen.setup(width=WIDTH , height= HEIGHT) 
screen.bgcolor("black")
screen.title("Mi Pong")


#Creamos y ubicamos los paddles:

player_1 = Paddles()
player_1.placement(w = WIDTH, place= "I", steps=STEPS)

player_2 = Paddles()
player_2.placement(w= WIDTH, place= "D", steps=STEPS)



screen.exitonclick()
