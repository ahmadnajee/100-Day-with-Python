
#name_of_user=input("Enter your name: ")  #str

#name_length=len(name_of_user)   #int

#print("The number of letters in your name: " + str(name_length)) #type conversion

#print( 3 *3 / 3 + 3 - 3 )

#height=float(input("enter your height in meter:"))

#weight=float(input("enter your weight in kg:"))

#BMI=weight/height**2

#print("your BMI is:",BMI)

print("welcome to tip calculator  !")

total_bill=int(input("what was the total bill? $"))

tip=int(input("How much would you like to give? 10, 12, 15"))

split_amount=int(input("How many people to split the bill? "))

bill_with_tip=total_bill+ ((total_bill*tip)/100)

calculator = bill_with_tip/split_amount
print(f"Each person should pay ${round(calculator,2 )}")