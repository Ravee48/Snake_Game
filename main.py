import time
from turtle import Screen
import snake
import food
import score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = score.Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increased_score()
        snake.extend()
        food.random_color()

    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_is_on = False
        score.game_over()

    for turtle in snake.all_turtle[1:]:
        # if turtle == snake.head:
        #     pass
        if snake.head.distance(turtle) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
