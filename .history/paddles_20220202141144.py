from turtle import Turtle
from main import STEP_ZISE 

class Paddles(Turtle):
    
    def __init__(self):
        super().__init__()

        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.speed(3)
        self.paddle.shapesize(stretch_len=5, stretch_wid=1)
        self.paddle.setheading(90)
    
    def placement(self, w, place, steps):
        
        if place == "I" or  place == "i":
            self.paddle.goto(x= -(w//2) + steps , y = 0)
        elif  place == "D" or place == "d":    
            self.paddle.goto(x= (w//2) - (steps + 10) , y = 0)    
          
    def up(self, steps):
        
        self.paddle.forward(steps*STEP_ZISE)
        
    def down(self, steps):
        
        self.paddle.backward(steps*STEP_ZISE)

        
        
        
          