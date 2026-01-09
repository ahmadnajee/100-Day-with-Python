import random
import art
from os import system

def deal_card():
    """ choose a random number from list of cards """
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """it takes a list of card as an input and calculate its total"""
    if sum(cards)==21 and len(cards)==2 :
         return 0   
    if 11 in cards and sum(cards)>21:
         cards.remove(11)
         cards.append(1)
         
    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:
        return "Draw  😐"
    elif c_score==0:
        return "Lose, opponent has a blackjack 🤦‍♂️😔"
    elif u_score==0:
        return "Win with a blackjack 🥇💰"
    elif u_score>21:
        return "You went over. You lose 😁🤦‍♂️"
    elif c_score>21:
        return "Opponent went over. You win 🤗😎"
    elif u_score>c_score:
        return "You win 🏆"
    else:
        return "You lose 😔"


def play_game():  
    print(art.logo)
    is_game_over=False
    users_cards=[]
    pc_cards=[]
    users_scores=-1
    pc_scores= -1
    for _ in range(2):
        users_cards.append(deal_card())
        pc_cards.append(deal_card())      
      
    while not is_game_over:      
        users_scores=calculate_score(users_cards)
        pc_scores=calculate_score(pc_cards)
        print(f"your cards: {users_cards}, your current score: {users_scores}")
        print(f"computers's first card: {pc_cards[0]}")
        if users_scores==0 or pc_scores==0 or users_scores>21:
            is_game_over=True
            
        else :
            should_continue=input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue=='y':
                users_cards.append(deal_card())
            else:
                is_game_over=True

    while pc_scores != 0 and pc_scores <17:
        pc_cards.append(deal_card())
        pc_scores=calculate_score(pc_cards)
        
    print(f"your final hand: {users_cards}, your final score: {users_scores}")
    print(f"computers final hand: {pc_cards}, computers final score: {pc_scores}")
    print(compare(users_scores,pc_scores))


while input("do you want to play a game of blackjack? type 'y' or 'n': ")=='y':
    system("cls")
    play_game()