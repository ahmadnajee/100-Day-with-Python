import art

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)



def caesar(direction,original_text, shift_number):
    if direction=="decrypt":
        shift_number *= -1
        
    cipher_text=""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        elif letter in alphabet :
            shift_position=alphabet.index(letter)+shift_number
            shift_position %=len(alphabet)
            cipher_text+=alphabet[shift_position]
        
    print(f"here is your {direction}d text {cipher_text}")
    
finish=False
while not finish:
    direction=input("type 'encode' to encrypt, type decode to decrypt: \n").lower()
    text=input("type your message: \n").lower()
    shift= int(input("type the shift number: \n"))
    caesar(direction=direction, original_text=text, shift_number=shift)
    
    user_answer=input( "do you want to continue??? type yes to continue. otherwise typue no ")
    if user_answer=="no":
        finish=True
        print("you have finish the application")

    
            
   


