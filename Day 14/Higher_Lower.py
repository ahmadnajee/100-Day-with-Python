import sys
import Game_Data
import art
from os import system
import random

#function to choose two random people from array

def chose_people():
   return random.choice(Game_Data.instagram_top_50)

def format_data(data):
    return f"{data["name"]}, a {data["description"]}, from {data["country"]}"

personA=chose_people()
personB=chose_people()

#shows its bio

print(art.logo)
game_over=False
score=0
while not game_over:
    print(f"Compare A: {format_data(personA)} ")
    print(f"Against B: {format_data(personB)} ")

    #assign its follower count into two variable A, B
    A=personA["follower_count"]
    B=personB["follower_count"]

    winner=""
    if A > B:
        winner="a"
    elif B > A:
        winner="b"
    else :
        print("Invalid choice")

    # Asks the user to choose a person
    user_answer=input("who has more followers? Type 'A' or 'B': ").lower()
    system("cls")

    # calculate the user answer
  
    if user_answer==winner:
        personA=personB
        personB=chose_people()
        score+=1    
        print(f"Correct! Your score is {score} ")
    else :
        game_over=True
        print(f"Sorry, it is wrong. Final score is {score}")






