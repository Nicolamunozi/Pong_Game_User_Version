from turtle import Screen, update
from paddles import Paddles
from ball import Ball
from constants import WIDTH, HEIGHT, SCREEN_COLOR, STEP_ZISE, ORIGIN


# 0) variables:


# I) Creando pantalla:  

screen = Screen()
screen.setup(width=WIDTH , height= HEIGHT) 
screen.bgcolor(SCREEN_COLOR)
screen.title("Mi Pong")
screen.tracer(0)
screen.delay(10)
# II) Creamos y ubicamos los paddles:

player_1 = Paddles()
player_1.placement(w = WIDTH, place= "I")

player_2 = Paddles()
player_2.placement(w= WIDTH, place= "D")


screen.update()
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

for _ in range(20):    
    screen.update()
    ball.ball_movement(6)



# player_1.up(1)
# player_1.down(5)

screen.exitonclick()
