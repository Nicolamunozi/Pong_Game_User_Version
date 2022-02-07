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


#definimos el uso de teclas, para mover los paddles:

screen.listen()

#Player 1:
screen.onkey(player_1.up(steps=2), "Up")
screen.onkey(player_1.down, "Down")

#Player 2:

screen.onkey(player_2.up, "w")
screen.onkey(player_2.down, "s")


# player_1.up(1)
# player_1.down(5)

screen.exitonclick()
