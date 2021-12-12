from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

LEVEL = 0.1

screen = Screen()
screen.title("The Pong Game.")
screen.listen()
screen.tracer(0)
screen.bgcolor("Black")
screen.setup(width=1000, height=600)

l_paddle = Paddle("Yellow", (-480, 0))
r_paddle = Paddle("Green", (480, 0))

ball = Ball()
scoreboard = Scoreboard()


game_on = True
while game_on:
    time.sleep(LEVEL)
    screen.update()
    ball.move()
    screen.onkeypress(l_paddle.up, "w")
    screen.onkeypress(l_paddle.down, "s")
    screen.onkeypress(r_paddle.up, "Up")
    screen.onkeypress(r_paddle.down, "Down")

    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_ball()

    if  ball.distance(r_paddle) < 90 and ball.xcor() > 455 or ball.distance(l_paddle) < 90 and ball.xcor() < -455:
        ball.bounce_x_ball()
        if LEVEL > .01667718169966658:
            LEVEL *= 0.9
    
    if ball.xcor() >495:
        scoreboard.l_point()
        ball.reset_game()
        scoreboard.game_reset()
        time.sleep(0.2)
        LEVEL = 0.1
    if ball.xcor() < -495:
        scoreboard.r_point()
        ball.reset_game()
        scoreboard.game_reset()
        time.sleep(0.2)
        LEVEL = 0.1
    
screen.exitonclick()