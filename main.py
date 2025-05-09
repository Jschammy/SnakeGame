# Import modules for game.
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Instantiate classes for screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Justin's Snake Game")
screen.tracer(0)

# Instantiate classes for snake, food, and the scoreboard.
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Listen to user input.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop.
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
