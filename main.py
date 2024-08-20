from turtle import Turtle, Screen
from paddle import Paddle
from blocks import Blocks
from ball import Ball
import time
import random

screen = Screen()
paddle = Turtle()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Breakout!")
screen.tracer(0)

paddle = Paddle((0, -220))
ball = Ball()

blocks = []
offset_x = 0
offset_y = 0
for i in range(30):
    block = Blocks(offset_x, offset_y)
    blocks.append(block)
    offset_x += 10
    offset_y += 5

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.distance(paddle) < 50 and ball.ycor() > -250:
        ball.bounce_x()
        ball.bounce_y()
        print(ball.bounce_y)

    for i, block in enumerate(blocks):
        if ball.distance(block) < 50:
            del blocks[i]
            block.hideturtle()
            ball.bounce_x()
            ball.bounce_y()

    if ball.xcor() > 370:
        ball.bounce_x()
        ball.bounce_y()


    if ball.xcor() < - 370:
        ball.bounce_x()
        ball.bounce_y()

    elif ball.ycor() > 280:
        ball.bounce_x()
        ball.bounce_y()

    elif ball.ycor() < -280:
       ball.goto(0, 0)
       ball.reset_ball()

    if ball.xcor() < - 395:
        ball.goto(0, 0)
        ball.reset_ball()

    if ball.xcor() > 395:
        ball.goto(0, 0)
        ball.reset_ball()


screen.exitonclick()