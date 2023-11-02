from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from specialfood import Specialfood
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
score = Scoreboard()
specialfood = Specialfood()
"""
Snake Game - Main Module

This module contains the main logic for the Snake Game. It sets up the game screen, initializes the snake, food, and scoreboard objects,
handles user input, and updates the game state.

The game loop runs until the snake collides with the wall or itself. When the game is over, the final score is displayed.

Controls:
- Up arrow key: Move snake up
- Down arrow key: Move snake down
- Left arrow key: Move snake left
- Right arrow key: Move snake right

"""


screen.onkey(snake.snake_up,"Up")
screen.onkey(snake.snake_down,"Down")
screen.onkey(snake.snake_left,"Left")
screen.onkey(snake.snake_right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    end_time = time.time()
    specialfood.toggle_size()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        specialfood.spawn_special_food()

    if (end_time - specialfood.start_time) >= 4:
        specialfood.hide()

    if snake.head.distance(specialfood) < 15:
        score.score = score.score + specialfood.score_adder
        score.update_scoreboard()
        specialfood.hide()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
        score.reset_score()
        snake.reset_snake()
        specialfood.hide()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
