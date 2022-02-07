from turtle import Screen
from paddles import Paddles
from ball import Ball
from score import Score, MiddleLine
from constants import ALIGNMET, FONT, WIDTH, HEIGHT, SCREEN_COLOR, STEP_ZISE, ORIGIN
import time 
import random

# 0) constantes:




# I) Creando pantalla:  

screen = Screen()
screen.setup(width=WIDTH , height= HEIGHT) 
screen.bgcolor(SCREEN_COLOR)
screen.title("Mi Pong")
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

#JUEGO:

#Funciones:

#Colision, player:
def is_collision_player(player_paddle=player_1.paddle, ball=ball.ball):

    player_x = player_paddle.xcor()
    player_y = player_paddle.ycor()
    ball_y = ball.ycor()
    ball_x = ball.xcor()
    
    collition = False
    
    if abs(ball_x - player_x) == STEP_ZISE:
        #Estamos en distancia de colision:
        for idx in range(4):
            if abs(ball_y - player_y) == idx * STEP_ZISE:
                #Estamos al alcance del paddle.
                collition = True
                
    return collition

                 
                     
 
#LOOP DEL JUEGO.

game_is_on = True
movement_states = [1,2,3,4,5,6]

while game_is_on:
    quadrant = random.choice(movement_states)
 
    while not ball.outside():
        time.sleep(0.900)
        screen.update()
    
        ball.move_ball(quadrant)
         
             
        if ball.wall_collision():
            if quadrant==1:
                quadrant=4
            elif quadrant==2:
                quadrant=3
            elif quadrant==3:
                quadrant=2 
            elif quadrant==4:
                quadrant=1                
        
        if is_collision_player(player_paddle=player_1.paddle):
            y_ball = ball.ball.ycor()
            y_player = player_1.paddle.ycor()
            if y_ball == y_player: 
                quadrant=5
            elif y_ball > y_player:
                quadrant=1    
            elif y_ball < y_player:
                quadrant=4 
                
        if is_collision_player(player_paddle=player_2.paddle):
            y_ball = ball.ball.ycor()
            y_player = player_2.paddle.ycor()
            if y_ball == y_player:
                quadrant = 6
            elif y_ball > y_player:
                quadrant = 2
            elif y_ball < y_player:
                quadrant = 3
                
        
    if ball.outside():
        if ball.ball.xcor()<0:
            score_player2.increase_score()
        else:
            score_player1.increase_score()
            
        ball.ball.goto(0,0)
       
        if score_player1.score== 10 or score_player2.score == 10:
            game_is_on = False
            ball.ball.write("GAME OVER", align=ALIGNMET, font=FONT)         
        


#mover pelota:
# player_1.up(3)
# pasos = (WIDTH//(2*STEP_ZISE)) 
# for _ in range(pasos):    
#     ball.ball_movement(6)


#Detectar colision pelota paddle, jugadores 1. 

#Funcion: 


    
# print(is_collision())    
# is_collision(player_paddle=player_2.paddle)





screen.exitonclick()
