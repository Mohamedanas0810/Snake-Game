#Snake Game
import turtle as T
import time
import snake
import food
import scoreboard
import border

turtle_body = []

#Screen 
Screen = T.Screen()
Screen.setup(width=600,height=600)

Screen.bgcolor("black")
Screen.title("Snake Game🐍")

Screen.listen()

#Border
border = border.Border()
border.draw_border()

# Scoreboard
scoreboard = scoreboard.ScoreBoard()

# Food
food = food.Food()

#Snake Body
snake = snake.Snake()

#Snake Movements
Screen.onkey(snake.move_up,"Up")
Screen.onkey(snake.move_down,"Down")
Screen.onkey(snake.move_left,"Left")
Screen.onkey(snake.move_right,"Right")

#Move Snake
game_on = True
while game_on:
    time.sleep(0.1)
    snake.move(snake.turtle_body)
    scoreboard.write

    #Check is food eaten
    if snake.head.distance(food) <15:
        food.new_food()
        snake.grow_snake()
        scoreboard.add_score()

    #Detect collison with the wall
    game_on = snake.detect_wall_collison()
    if game_on == False:
        scoreboard.game_over()
        break
      
    #Detect collison with tail
    game_on = snake.detect_collison_with_tail()
    if game_on == False:
        scoreboard.game_over()

Screen.exitonclick()