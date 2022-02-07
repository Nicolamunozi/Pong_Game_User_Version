from turtle import Turtle
from constants import STEP_ZISE 

class Paddles(Turtle):
    
    def __init__(self):
        super().__init__()

        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.speed(0)
        self.paddle.shapesize(stretch_len=5, stretch_wid=1)
        self.paddle.setheading(90)
    
    def placement(self, w, place):
        
        if place == "I" or  place == "i":
            self.paddle.goto(x= -(w//2) + STEP_ZISE , y = 0)
        elif  place == "D" or place == "d":    
            self.paddle.goto(x= (w//2) - STEP_ZISE , y = 0)    
          
    def up(self, steps=1):
        
        self.paddle.forward(steps*STEP_ZISE)
        
    def down(self, steps=1):
        
        self.paddle.backward(steps*STEP_ZISE)

        
        
        
          