from turtle import Turtle

class Paddles(Turtle):
    
    def __init__(self):
        super().__init__()

        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.speed(1)
        self.paddle.shapesize(stretch_len=5, stretch_wid=1)
        self.paddle.heading(90)
        