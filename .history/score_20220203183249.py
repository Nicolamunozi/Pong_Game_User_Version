from turtle import Turtle
from constants import WIDTH, HEIGHT

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = Turtle("turtle") 
        self.score.color("white")
    