from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()

screen.listen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.back(10)


def turn_left():
    new_heading=timmy.heading()+10
    timmy.setheading(new_heading)



def turn_right():
      new_heading=timmy.heading()-10
      timmy.setheading(new_heading)


def home():
    timmy.up()
    timmy.clear()
    timmy.home()
    timmy.down()


screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=home)


screen.exitonclick()