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
print(player_1.get_shapepoly())
player_1.shapesize(stretch_wid= 3*STEPS , stretch_len= STEPS)





screen.exitonclick()
