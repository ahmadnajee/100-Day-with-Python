import turtle
import random

AREA = 360
STEP = 100
colors=["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]


timmy= turtle.Turtle()
turtle.colormode(255)
timmy.shape("turtle")

timmy.speed(5)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# def draw_shape(num_sides) :
#     angle = AREA / num_sides
#     for _ in range(num_sides):
#         timmy.forward(STEP)
#         timmy.right(angle)  
        
        
# directions=[0,90,180,270]
# for _ in range(200):

#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
      
timmy.speed("fastest")
timmy.pensize(3)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):   
        timmy.color(random_color())     
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(10)
        
screen= turtle.Screen()
screen.exitonclick()