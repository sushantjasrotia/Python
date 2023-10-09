from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height=600)
screen.title("Pong")
screen.tracer(0) # turn off the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
Ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True  #due to tracer function we have to update screen manually
while game_is_on:
    time.sleep(Ball.move_speed)
    screen.update()
    Ball.move()

    #detecting collision with ball
    if Ball.ycor() > 280 or Ball.ycor() < -280:
        Ball.bounce_y()

    #Detect collision with  paddles
    if Ball.distance(r_paddle) < 50 and Ball.xcor() > 320 or Ball.distance(l_paddle) < 50 and Ball.xcor() < -320:
        Ball.bounce_x()

    #Detect when r_paddle miss the ball
    if Ball.xcor() > 380:
        Ball.reset_position()
        scoreboard.l_point()

    #detect l_paddle miss
    if Ball.xcor() < -380:
        Ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()
