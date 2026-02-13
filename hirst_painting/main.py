import turtle 
import random

colors_list=[  (236, 224, 81), (197, 7, 72), (201, 75, 15), (113, 178, 214), (196, 164, 13), (231, 54, 132)]
turtle.colormode(255)
timmy= turtle.Turtle()
timmy.hideturtle()

timmy.setheading(225)
timmy.up()
timmy.forward(300)
timmy.setheading(0)

for _ in range(10):
    for i in range(10):
        timmy.dot(20,random.choice(colors_list))
        timmy.up()
        timmy.forward(50)
    
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)
  
   


screen=turtle.Screen()
screen.exitonclick()