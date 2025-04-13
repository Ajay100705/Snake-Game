from turtle import Turtle, Screen
from snake import Snake
import time
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()


screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        print("food eaten")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    # Detect collision with tail.
    # for segment in snake.segments:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        # # If head collides with any segment in the tail : Trigger game_over.
        #     game_is_on = False
        #     scoreboard.game_over()

        # Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.segments:
                pass
                # If head collides with any segment in the tail : Trigger game_over.
            elif snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()


screen.exitonclick()