from turtle import Screen
from paddles import Paddles
from ball import Ball
from score import Score, MiddleLine
from constants import WIDTH, HEIGHT, SCREEN_COLOR, STEP_ZISE, ORIGIN

# 0) constantes:


# I) Creando pantalla:  

screen = Screen()
screen.setup(width=WIDTH , height= HEIGHT) 
screen.bgcolor(SCREEN_COLOR)
screen.title("Mi Pong")
screen.delay(20)
screen.tracer(0)


# XI) Score y linea de en medio:

score_player1 = Score(1)
score_player2 = Score(2)
mid = MiddleLine()

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


# IV) Crear pelota. 

#Pelota creada:

ball = Ball()

ball.ball.move_ball(1)

print(ball.wall_collision())

#Pelota fuera del  mapa, aumentar score (Prueba):

if ball.outside():
    if ball.ball.xcor()<0:
        score_player2.increase_score()
    else:
        score_player1.increase_score()    
    


#mover pelota:
# player_1.up(3)
# pasos = (WIDTH//(2*STEP_ZISE)) 
# for _ in range(pasos):    
#     ball.ball_movement(6)


#Detectar colision pelota paddle, jugadores 1. 

#Funcion: 

def is_collision_player(player_paddle = player_1.paddle, ball=ball.ball):
    
    player_y = player_paddle.ycor()
    ball_y = ball.ycor()
    
    if player_paddle.distance(ball) < 65:
        if player_y == ball_y:
            if player_paddle.distance(ball) <25:
                return True             
            else:
                return False 
        elif player_y == ball_y + STEP_ZISE  or player_y == ball_y - STEP_ZISE:
            if player_paddle.distance(ball) < 30:
                return True
            else:
                return False  
        elif player_y == ball_y + 2*STEP_ZISE or player_y == ball_y - 2*STEP_ZISE:
            if player_paddle.distance(ball) < 45:
                return True
            else: 
                return False       
        else: 
            return True         
    else: 
        return False 
    
# print(is_collision())    
# is_collision(player_paddle=player_2.paddle)





screen.exitonclick()
