from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800 , height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle(350 , 0)
l_paddle = Paddle(-350 , 0)
ball = Ball()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(fun=l_paddle.go_up, key= "w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
        
    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x() 
        
    # If the ball missed
    if ball.xcor() > 380 :
        ball.reset_ball()
        scoreBoard.l_point()
    
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreBoard.r_point()    
    
    
screen.exitonclick()