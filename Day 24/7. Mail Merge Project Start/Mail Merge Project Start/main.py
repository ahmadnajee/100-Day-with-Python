PLACEHOLDER = "[name]"
with open("./Day 24/7. Mail Merge Project Start/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Day 24/7. Mail Merge Project Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    
    for name in names_list:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Day 24/7. Mail Merge Project Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}", "w") as completed_letter:
            completed_letter.write(new_letter)
            
    


