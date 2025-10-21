from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 18 , "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,260)
        self.color('white')
        self.write(f"Score: {self.score}",move=False,align=ALIGNMENT,font=FONT)
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",move=False,align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game Over!",align=ALIGNMENT,font=FONT,move=False)
        
