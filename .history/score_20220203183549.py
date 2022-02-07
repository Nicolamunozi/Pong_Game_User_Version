from turtle import Turtle
from constants import WIDTH, HEIGHT, STEP_ZISE

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = Turtle("turtle") 
        self.score.color("white")
        self.score.penup()
        self.score.goto(0, HEIGHT//2 - STEP_ZISE)