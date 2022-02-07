from turtle import Turtle, Screen
from paddles import Paddles

#CONSTANTES:

WIDTH =  50
HEIGHT =  50
SCREEN_COLOR =  "black" 
STEPS = 20

#Creando pantalla:  

screen = Screen()
screen.setup(width=WIDTH , height= HEIGHT) 
screen.bgcolor("black")
screen.title("Mi Pong")


#Creamos y ubicamos los paddles:

player_1 = Paddles()
player_1.paddle.goto(x= -(WIDTH//2) + 10 , y = 0)
player_1.placement(w = WIDTH, place= "I")

player_2 = Paddles()
player_2.placement(w= WIDTH, place= "D")

# player_2 = Turtle("square")
# player_2.color("white")
# player_2.penup()
# player_2.speed(1)
# player_2.shapesize(stretch_len= 5, stretch_wid= 1)
# player_2.setheading(90)
# player_2.goto(x = (WIDTH//2) - 20, y =0)

screen.exitonclick()
