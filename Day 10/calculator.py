from os import system
def add(n1,n2):
    return n1+ n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1/n2


operations={
    "+": add,
    "-":substract,
    "*":multiply,
    "/":division
}
def calculator():
    should_accumulate=True
    number1=float(input("type your first number: "))

    while should_accumulate:
    
        for x in operations:
            print(x)
        operator=input("choose an operation:")
        number2=float(input("Enter your second number: "))
        
        result=operations[operator](number1,number2)
        print(f"{number1} {operator} {number2} = {result}")
        choice=input(f"type 'y' to continue calculating with {result}, 'n' for strating new calculation").lower()
        if choice=="y":
            number1=result
        else :
            system("cls")
            should_accumulate=False
            calculator()
    
 
calculator()  

    



 