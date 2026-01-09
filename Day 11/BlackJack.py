import random
score_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]
pc_range_of_choices=[1,2,3,4,5,]
game_over=False
user_choice=input("Do you want to play a game of black jack? type 'y' or 'n': ")
if user_choice=='n':
    game_over=True
    
while not game_over:
    user_scores=[]
    sum_of_user_scores=0
    pc_scores=[]
    sum_of_pc_scores=0
    #users random choices
    for num in range(0,2):
        user_scores.append(random.choice(score_list))
        
    #pc random choices
    for num in range(0,random.choice(pc_range_of_choices)):
         pc_scores.append(random.choice(score_list))
         
         
    for n in user_scores:
        sum_of_user_scores+=n
        
    for n in pc_scores:
        if sum_of_pc_scores < 21:
            sum_of_pc_scores+=n
        
    print(f"Your cards: {user_scores}, current scores: {sum_of_user_scores}")
    print(f"Computer's first card: {pc_scores[0]}")
    
    should_continue=input("Type 'y' to get another card, type 'n' to pass: ")
    if should_continue=='n':
        if sum_of_pc_scores<21 and sum_of_user_scores < 21:
            if sum_of_user_scores==sum_of_pc_scores:
                print("Draw")
                print(f"Your scores{user_scores}={sum_of_user_scores}")
                print(f"pc scores{pc_scores}={sum_of_pc_scores}")
                
            elif sum_of_user_scores > sum_of_pc_scores :
                print("You win!!! 🥇💰🏆")
                print(f"Your scores{user_scores}={sum_of_user_scores}")
                print(f"pc scores{pc_scores}={sum_of_pc_scores}")
                
            else :
                print("You lose!!😔😞")
                print(f"Your scores{user_scores}={sum_of_user_scores}")
                print(f"pc scores{pc_scores}={sum_of_pc_scores}")
                
        elif sum_of_user_scores >21:
            print("you went over!!\n you lose")
            print(f"Your scores{user_scores}={sum_of_user_scores}")
            print(f"pc scores{pc_scores}={sum_of_pc_scores}")
                
        elif sum_of_pc_scores >21  :
            print("you win 🥇, the opponent went over!!")
            print(sum_of_pc_scores)
            print(f"Your scores{user_scores}={sum_of_user_scores}")
            print(f"pc scores{pc_scores}={sum_of_pc_scores}")
                
        game_over=True             
    elif should_continue=='y':
        for num in range(0,1):
            user_scores.append(random.choice(score_list))
        
        for n in user_scores:
            sum_of_user_scores+=n
     
        
    game_over=True
    
    
    