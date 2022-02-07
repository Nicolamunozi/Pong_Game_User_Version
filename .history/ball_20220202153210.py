from turtle import Turtle
from constants import STEP_ZISE
from math import pi, sin, cos




class Ball(Turtle):  
    def __init__(self):
        super().__init__()
        
        self.ball = Turtle("circle")
        self.ball.speed(3)
        self.ball.color("white")
        
        #para el movimiento de la pelota. 
        self.Y_STEP = sin(45* pi/180) * STEP_ZISE
        self.X_STEP = cos(45* pi/180) * STEP_ZISE 
        
    def ball_movement(self):
        
        #Posicion incial de la pelota:
        self.position_x = self.ball.xcor()
        self.position_y = self.ball.ycor()        
        self.ball.goto(self.position_x + self.X_STEP, self.position_y + self.Y_STEP)    

