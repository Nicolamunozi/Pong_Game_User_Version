from turtle import Turtle, Screen

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


#Crear los paddles:

player_1 = Turtle("square")
player_1.color("white")
player_1.speed(1)
player_1.shapesize(stretch_len= 5, stretch_wid=1)
player_1.setheading(90)
player_1.goto(x= -200, y = 0)


screen.exitonclick()
