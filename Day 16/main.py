# from turtle import Turtle, Screen


# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)


# myScreen=Screen()
# myScreen.exitonclick()

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"],"l")
table.add_column("Type ", ["Electric", "Water", "Fire"],"l")
print(table)