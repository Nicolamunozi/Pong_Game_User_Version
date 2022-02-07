from turtle import Turtle
from constants import WIDTH, HEIGHT, STEP_ZISE, ALIGNMET, FONT



class Score(Turtle):
    
    def __init__(self, player):
        super().__init__()
            
        self.text = Turtle("turtle")
        self.text.color("white")
        #self.text.hideturtle()
        self.text.penup()
        self.score = 0
        
        if player == 1: 
            self.text.goto(-WIDTH//4, HEIGHT//2 - 2*STEP_ZISE)
        
        
        
        self.text.write(self.score, align=ALIGNMET, font= FONT)
        
        
    def increase_score(self):

        self.score += 1
        