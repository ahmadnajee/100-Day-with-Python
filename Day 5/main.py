import random
# student_scores=[90,78,100,94,89,93,120,90,87 ,99,120,140]
#
# highest_score=0
#
# for score in student_scores:
#      if score > highest_score:
#          highest_score=score
#
# print(highest_score)


# number=0
# for i in range(1, 101):
#     number+=i
#
# print(number)

#
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#        print(i)

letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*']

print("welcome to pyPassword generator")
nr_letters=int(input("how many letters would you like to have in ur password?"))
nr_numbers=int(input("how many numbers would you like to have in ur password?"))
nr_symbols=int(input("how many symbols would you like to be in ur password?"))


random_letter=[]
for letter in range(nr_letters):
    random_letter.append(random.choice(letters))

random_number=[]
for number in range(nr_numbers):
    random_number.append(random.choice(numbers))

random_symbol=[]
for symbol in range(nr_symbols):
    random_symbol.append(random.choice(symbols))

password=random_letter+random_number+random_symbol
print(password)
random.shuffle(password)

print(password)

password2=""
for char in password:
    password2 +=char

print("Here is ur unhackable password: "+ password2)