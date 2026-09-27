import turtle
import pandas

# Reading data from csv file
data = pandas.read_csv("./5. day-25-us-states-game-start/50_states.csv")

# Building the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./5. day-25-us-states-game-start/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# Create a separate turtle for writing
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

states = data["state"]

gussing_states = []

# User's input
while len(gussing_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(gussing_states)}/50 States Correct",
        prompt="What is another state: "
    )

    if answer_state == "Exit":
        states_to_learn = [state for state in states if state not in gussing_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("./5. day-25-us-states-game-start/states_to_learn.csv")
        break
    
    answer_title = answer_state.title()
    for state in states:
        if answer_title == state:
            print(answer_title)
            gussing_states.append(answer_title)
            state_data = data[data.state == answer_title]
            x = state_data.x.item()
            y = state_data.y.item()
            writer.goto(x, y)
            writer.write(answer_title)

screen.exitonclick()