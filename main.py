from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

MAX_WALL = 280
MIN_WALL = -280

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # eating food:
    if snake.head.distance(food) < 15:
        # food new location
        # snake get bigger
        food.new_food()
        snake.snake_bigger()
        score.update_score()

    # walls:
    if snake.head.xcor() > MAX_WALL or snake.head.xcor() < MIN_WALL or snake.head.ycor() > MAX_WALL or\
            snake.head.ycor() < MIN_WALL:
        score.reset()
        snake.snake_reset()

    # tail:
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            score.reset()
            snake.snake_reset()


screen.exitonclick()
