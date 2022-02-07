from turtle import Turtle
from constants import STEP_ZISE

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.ball = Turtle("circle")
        self.ball.speed(3)
        self.ball.color("white")
        
        
        