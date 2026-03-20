import turtle as t
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

snake = Snake()
food = Food()
score_board = Scoreboard()

screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score_board.update_score()
    # Detect collision with food
    if snake.head.distance(food) <15 :
        food.refresh()
        snake.extent()
        score_board.increase_score()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()




screen.exitonclick()
