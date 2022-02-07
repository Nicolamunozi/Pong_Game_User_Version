from turtle import Turtle
from constants import WIDTH, HEIGHT, STEP_ZISE, ALIGNMET, FONT



class Score(Turtle):
    
    def __init__(self, player):
        super().__init__()
            
        self.text = Turtle("turtle")
        self.text.color("white")
        self.text.hideturtle()
        self.text.penup()
        self.score = 0
        
        if player == 1: 
            self.text.goto(-WIDTH//4, HEIGHT//2 - 3*STEP_ZISE)
        else: 
            self.text.goto(WIDTH//4, HEIGHT//2 - 3*STEP_ZISE)

        self.refresh_score()
        
        
    def increase_score(self):

        self.score += 1
        self.refresh_score()
        
    def refresh_score(self):
        
        self.text.clear()
        self.text.write(self.score, align=ALIGNMET, font=FONT)

            
class MiddleLine(Turtle):
        
    def __init__(self):
        super().__init__()
        
        self = Turtle("turtle")
        self.color("white")
        self.hideturtle()
        self.setheading(90)
        self.forward((HEIGHT//2)) 
        self.setpos(0,0)  
        self.back((HEIGHT//2))          