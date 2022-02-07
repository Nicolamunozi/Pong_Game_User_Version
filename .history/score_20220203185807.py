from turtle import Turtle
from constants import WIDTH, HEIGHT, STEP_ZISE, ALIGNMET, FONT



class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = Turtle("turtle") 
        self.score.color("white")
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0, HEIGHT//2 - 2*STEP_ZISE)
        self.score.write("Score: ", align=ALIGNMET, font= FONT)