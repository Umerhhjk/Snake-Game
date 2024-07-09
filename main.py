import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_continue = True
while game_continue:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        snake.new_segment()


screen.exitonclick()
