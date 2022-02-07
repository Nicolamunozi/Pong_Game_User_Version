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
        
        self.mid = Turtle("turtle")
        self.mid.color("white")
        self.mid.hideturtle()
        self.mid.setheading(90)
        self.movement_line()
        self.mid.penup()
        self.mid.setpos(0, 0)   
        self.mid.setheading(270)
        self.movement_line()

    def movement_line(self):

        steps = (HEIGHT//2) // STEP_ZISE
        
        for step in range(steps):
            if step%2 == 0:    
                self.mid.forward(STEP_ZISE)
                self.mid.penup()        
            else:
                self.mid.forward(STEP_ZISE)
                self.mid.pendown()
        
        