from turtle import Turtle
from constants import WIDTH, HEIGHT, STEP_ZISE, ALIGNMET, FONT



class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.text = Turtle("turtle") 
        self.text.color("white")
        self.text.hideturtle()
        self.text.penup()
        self.text.goto(0, HEIGHT//2 - 2*STEP_ZISE)
        self.text.write("Score: ", align=ALIGNMET, font= FONT)
        
        
    def increase_score(self):
        pass 