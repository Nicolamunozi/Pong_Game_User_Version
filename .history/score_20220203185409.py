from turtle import Turtle
from constants import WIDTH, HEIGHT, STEP_ZISE

SCORE_SIZE = int((WIDTH+HEIGHT) * 0.01875)
FONT = ('Courier', SCORE_SIZE , 'bold')
ALIGNMET = "center"

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = Turtle("turtle") 
        self.score.color("white")
        self.score.penup()
        self.score.goto(0, HEIGHT//2 - 2*STEP_ZISE)
        self.score.write("Score: ", align=ALIGNMET, font= FONT)