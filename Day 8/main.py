def life_in_weeks(age):
    remaining_Age=90-age
    remaining_weeks=remaining_Age*12*4
    print(f"You have {remaining_weeks} weeks left")

life_in_weeks(19)

def greet_with(name, location):
    print(f"hello {name}")
    input(f" what is it like in {location}")


greet_with(location="Balkh", name="Ahmad")