import random


word_list=["aardvark","baboon", "camel"]
lives=6

chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""

for letter in chosen_word:
    placeholder+="_"
print(placeholder)

game_over=False
correct_letters=[]

while not game_over :

    chosen_letter=input("guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter==chosen_letter:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
             display+=letter
        else :
            display+="_"


    print(display)
    if chosen_letter not in chosen_word:
        lives-=1
        if lives==0:
            print("You lose!")
            game_over=True
    if "_" not in display:
        print("You win!")
        game_over=True
