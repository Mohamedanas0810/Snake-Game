from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('RoyalBlue')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        x_cor = random.randint(-240,240)
        y_cor = random.randint(-240,240)
        self.goto(x_cor,y_cor)
    
    def new_food(self):
        x_cor = random.randint(-240,240)
        y_cor = random.randint(-240,240)
        self.goto(x_cor,y_cor)