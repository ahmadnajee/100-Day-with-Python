import random

# number=random.randint(0,1)
#
# if number==0:
#     print("Head")
# else:
#     print("Tail")

# friends=["Basir", "Ahmad", "Qasim", "Ali Reza", "Hayat"]
# print(random.choice(friends))
#
#
# random=random.randint(0, len(friends)-1)
# print(friends[random])
#




paper= '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors=  '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


'''

rock=  '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
game=[paper, scissors, rock]
user_number=int(input("which one u want to choose? 0 for paper, 1 for scissor, 2 for rock"))
user_choice=game[user_number]
pc_number=random.randint(0,2)
pc_choice=game[pc_number]
if user_number >2 and user_number<0:
    print("Invalid choice")
elif user_number ==pc_number:
    print("draw")
elif user_number==0 and pc_number==2:
    print("You win")
elif user_number > pc_number==0:
    print("You win")
elif user_number < pc_number:
    print("You lose")






print("Your choice: "+ user_choice)
print(pc_choice)


