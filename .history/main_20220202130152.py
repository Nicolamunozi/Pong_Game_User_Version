from turtle import Turtle, Screen

#CONSTANTES:

WIDTH =  400
HEIGHT =  600
SCREEN_COLOR =  "black" 
STEPS = 20

#Creando pantalla:  

screen = Screen()
screen.screensize(canvwidth= WIDTH  , canvheight= HEIGHT , bg= SCREEN_COLOR ) 
screen.title("Mi Pong")


#Crear los paddles:

player_1 = Turtle("square")
player_1.color("white")
player_1.speed(1)
player_1.shapesize(stretch_len= 5, stretch_wid=1)
player_1.setheading(90)


screen.exitonclick()
