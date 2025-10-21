import turtle

class Border:
    def __init__(self):
        self.shadow = turtle.Turtle()
        self.shadow.hideturtle()
        self.shadow.shape('turtle')
        self.shadow.color('white')
        self.shadow.penup()
        self.heading = 0
    
    def draw_border(self):
        for _ in range(6):
            if self.heading == 0:
                self.shadow.goto(270,0)
                self.shadow.pendown()
                self.shadow.setheading(self.heading)
            elif self.heading == 90:
                self.shadow.goto(270,260)
                self.shadow.setheading(self.heading)
            elif self.heading == 180:
                self.shadow.goto(-280,260)
                self.shadow.setheading(self.heading)
            elif self.heading == 270:
                self.shadow.goto(-280,-260)
                self.shadow.setheading(self.heading)
            elif self.heading == 360:
                self.shadow.goto(270,-260)
                self.shadow.setheading(self.heading)
            elif self.heading == 450:
                self.shadow.goto(270,0)
            self.heading += 90


