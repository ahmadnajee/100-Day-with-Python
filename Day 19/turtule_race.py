from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_beat = screen.textinput(title="Make your beat", prompt="Which turtle will win the race? enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = 100

for turtle in range(0,6):
    new_turtle = Turtle(shape="turtle" )
    y = y - 30
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x = -230, y = y )
    all_turtles.append(new_turtle)
    
if user_beat:
    is_race_on = True

while is_race_on : 
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_beat: 
                print(f"You've win, the {winning_color} turtle is the winner!!")
            else:
                print(f"You've lost, the {winning_color} turtle is the winner!!")
                
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()
