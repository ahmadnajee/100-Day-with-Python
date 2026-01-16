from random import randint
from art import logo


EASY_LEVEL_TURNS=5
HARD_LEVEL_TURNS=10

#Function to user's guess against computer's guess
def check_guess(user_answer, actual_answer, turns):
    if user_answer > actual_answer:
        print("too high")
        return turns - 1 
    elif user_answer < actual_answer:
        print("too low")
        return turns - 1
    else :
        print(f"you got it, the answer is correct. Answer {actual_answer}")
        
        
# Function to set difficulty
def set_difficulty():
    level= input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
    if level =="easy":
        return EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS
def game():   
    print(logo)

    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1,100)

    print(f"the correct answer is {answer}")

    turns = set_difficulty()
    print(turns)

    # Let the user to guess 
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number. ")    
        guess = int(input("Make a guess: "))
        turns=check_guess(guess, answer, turns)
        
        if turns == 0 :
            print("You have run out of guesses. You lose!!")
            return
        elif guess != answer :
            print("Guess again!s")

game()