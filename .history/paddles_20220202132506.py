from turtle import Turtle

class Paddles(Turtle):
    
    def __init__(self):
        super().__init__()

        self.paddle = Turtle("Square")
        self.paddle.color("white")
        self.penup()
        self.speed(1)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.heading(90)