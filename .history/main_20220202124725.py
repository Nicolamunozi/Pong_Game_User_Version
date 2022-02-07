from turtle import Turtle, Screen

#CONSTANTES:

WIDTH =  400
HEIGHT =  600
SCREEN_COLOR =  "black" 

#Creando pantalla:  

screen = Screen()
screen.screensize(canvwidth= WIDTH  , canvheight= HEIGHT , bg= SCREEN_COLOR ) 
screen.title("Mi Pong")


#Crear los paddles:

player_1 = Turtle("square")
player_1.color("white")
player_1.speed(1)
print(player_1.get_shapepoly())
player_2 = Turtle("square")
player_2.color("red")
player_2.speed(1)
player_2.forward(20)
player_1.forward(40)








screen.exitonclick()
