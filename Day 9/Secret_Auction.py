from os import system

def highest_bid(bid):
    highest_bid=0
    winner=""
    for bidder in bid:
        bid_amount=bid[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid[bidder]
            winner=bidder
            
    print(f" the winner is {winner} with {highest_bid} $$")         
bid_info={}
finish_the_program=False
while not finish_the_program:
    
    name=input("What is ur name?  ")
    bid_value=int(input("What's ur bid? "))
  
    bid_info[name]=bid_value
    
    should_continue=input("is there any other person?  yes or no ")

    if should_continue=="yes":
        system("cls")
    else : 
        highest_bid(bid_info)
        finish_the_program=True

