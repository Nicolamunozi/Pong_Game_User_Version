from turtle import Screen
from paddles import Paddles
from ball import Ball
from constants import WIDTH, HEIGHT, SCREEN_COLOR, STEP_ZISE, ORIGIN
import time 

# 0) variables:


# I) Creando pantalla:  

screen = Screen()
screen.setup(width=WIDTH , height= HEIGHT) 
screen.bgcolor(SCREEN_COLOR)
screen.title("Mi Pong")
screen.delay(20)
screen.tracer(0)


# II) Creamos y ubicamos los paddles:

player_1 = Paddles()
player_1.placement(w = WIDTH, place= "I")

player_2 = Paddles()
player_2.placement(w= WIDTH, place= "D")


# III) Mover paddles con las teclas:

screen.tracer(1)
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

pasos = (WIDTH//(2*STEP_ZISE)) - 2

print(pasos)
player_1.down(steps=1)
for _ in range(pasos):    
    ball.ball_movement(6)

print(f" esto es la posicion del paddle {player_1.paddle.pos()}, esto es la posicion de la pelota {ball.ball.pos()}")
print(f"{ball.ball.distance(player_1.paddle.pos())} esto es la distancia entre la bola y el paddle")


# player_1.up(1)
# player_1.down(5)

screen.exitonclick()
