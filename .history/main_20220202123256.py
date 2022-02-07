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

player_1 = Turtle("turtle")
player_1.color("white")

player_1.speed(1)

for _ in range(3):
    player_1.forward(200)
    player_1.backward(200)
    h = player_1.heading()
    print(h)
    player_1.setheading(h + 90)
    

player_1.forward(200)
player_1.backward(200)
print(player_1.heading())
player_1.setheading(90)
player_1.forward(200)
player_1.backward(200)
print(player_1.heading())
player_1.setheading(180)
player_1.forward(200)
player_1.backward(200)
print(player_1.heading())
player_1.setheading(270)
player_1.forward(200)
player_1.backward(200)
print(player_1.heading())




player_1.setheading(0)
print(player_1.heading())















screen.exitonclick()
