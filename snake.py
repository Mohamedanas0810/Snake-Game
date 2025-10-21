import turtle as T
import time

# Constants
STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Screen 
Screen = T.Screen() 

class Snake:
    def __init__(self):
        self.turtle_body = self.snake_body()
        self.head = self.turtle_body[0]

    #Snake Body
    def snake_body(self):
        self.turtle_body = []
        x, y = 0,0
        Screen.tracer(0)
        for _ in range(3):
            segment = T.Turtle()
            segment.shape('square')
            segment.color('white')
            segment.speed('slowest')
            segment.penup()
            segment.setposition(x,y)
            x -=20
            self.turtle_body.append(segment)
        Screen.update()
        return self.turtle_body
    
    #Turtle actions

    #Move forward
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)    

    #Move left
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    #Move right
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    #Move down
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    #Start the snake movement
    def move(self,turtle_body):
        Screen.tracer(0)
        for seg in range(len(turtle_body)-1,0,-1):
            segment = turtle_body[seg]
            pre_segment = turtle_body[seg -1]
            seg_pos = pre_segment.pos()
            segment.goto(seg_pos)
        turtle_body[0].forward(STEPS)
        Screen.update()

    # Grow snake
    def grow_snake(self):
        segment = T.Turtle()
        segment.shape('square')
        segment.color('white')
        segment.speed('slowest')
        segment.penup()
        self.turtle_body.append(segment)

    #Detect Wall collison
    def detect_wall_collison(self):
        if self.head.xcor() > 250 or self.head.xcor() < -260 or self.head.ycor() > 250 or self.head.ycor() < -250:
            return False
        else:
            return True
    
    #Detect collison with tail
    def detect_collison_with_tail(self):
        for seg in range(1,len(self.turtle_body)):
            snake_seg = self.turtle_body[seg]
            if self.head.distance(snake_seg) < 10:
                return False
        return True
