from sqlite3 import enable_shared_cache
from turtle import Turtle
from constants import STEP_ZISE, WIDTH
from math import pi, sin, cos




class Ball(Turtle):  
    def __init__(self):
        super().__init__()
        
        self.ball = Turtle("circle")
        self.ball.penup()
        self.ball.speed(5)
        self.ball.color("white")
        
        #para el movimiento de la pelota. 
        self.Y_STEP = sin(45* pi/180) * STEP_ZISE
        self.X_STEP = cos(45* pi/180) * STEP_ZISE 
        
    def ball_movement(self, cuadrante):
                       
        #Posicion incial de la pelota:
        self.position_x = self.ball.xcor()
        self.position_y = self.ball.ycor()        
        
        if cuadrante == 1: 
            #sube en x e y. 
            self.ball.goto(self.position_x + self.X_STEP, self.position_y + self.Y_STEP)    
        elif cuadrante == 2:
            #baja en x, sube en y.    
            self.ball.goto(self.position_x - self.X_STEP, self.position_y + self.Y_STEP)
        elif cuadrante == 3:
            #baja en x e y. 
            self.ball.goto(self.position_x - self.X_STEP, self.position_y - self.Y_STEP)
        elif cuadrante == 4: 
            #baja en y, sube en x.
            self.ball.goto(self.position_x + self.X_STEP, self.position_y - self.Y_STEP)  
        elif cuadrante == 5: 
            #se mantiene en y, sube en x. 
            self.ball.goto(self.position_x + STEP_ZISE, self.position_y)  
        else: 
            #se mantiene en y, baja en x
            self.ball.goto(self.position_x - STEP_ZISE, self.position_y)  
        
    def outside(self): 
        """ This function is for get boolean values for the cases in which the ball is outside
        or inside the canvas."""
        
        ball_x = self.ball.xcor() 
                 
        if ball_x == -WIDTH//2 or ball_x == WIDTH//2 - STEP_ZISE:
            return True 
        else: 
            return False
            
            #a la izquierda en WIDTH //2 
            #a la derecha en WIDTH//2 - STEP_SIZE 