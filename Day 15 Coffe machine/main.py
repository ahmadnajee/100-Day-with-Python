MENU={
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}
resources={
    "water":200,
    "milk":200,
    "coffee":100,
    "money": 0
}
#TODO: 1. print the existing resource
def report():
    for i in resources:
        print( f" {i}: {resources[i]}")
    
# TODO: 2. check the resources
def check_resource(ordered_item,resources):
    '''
    it check wether there is enough resource or no
    :param ordered_item: the item that is ordered by the user
    :param resource: dictionary of the resource
    '''
    for i in MENU[ordered_item]["ingredients"] and resources:
        if i == "money":
            continue
        if MENU[ordered_item]["ingredients"][i] > resources[i]:
            return False
        return True    
#TODO: 3. process the coins
def process_coin(quarters, dimes, nickles, pennies):
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total

#TODO: 4. give the cost of each coffee
def coffee_cost(coffee):
    return MENU[coffee]["cost"]

# TODO. 5. check the successes of the transaction


def check_transaction(user_coins, coffee_cost):
    if user_coins < coffee_cost:
        return False
    elif user_coins == coffee_cost or user_coins > coffee_cost :
    
        resources["money"] += user_coins
        return True



#TODO: 5. make coffee
def make_coffee(coffee):
    '''
    it make the coffee that the user wants
    
    :param coffee: the coffee of the user
    '''
   
    for i in MENU[coffee]["ingredients"]:
        resources[i] = resources[i]-MENU[coffee]["ingredients"][i]
    
    
    
    
    
is_off=False


while not is_off:
    user_coffee=input("What would you like? (espresso/ latte/ cappuccino) ").lower()
    if user_coffee=="off":
        is_off = True
    elif user_coffee == "report":
        report()
    elif user_coffee:
        if check_resource(user_coffee, resources):
            print("Please insert coins.")
            quarter = int(input("how many quarter: "))
            dimes = int(input("how many quarter: "))
            nickles = int(input("how many quarter: "))
            pennies = int(input("how many quarter: "))
            cost=coffee_cost(user_coffee)
            inserted_coins= process_coin(quarter, dimes, nickles, pennies)
            print(f"here is your coins ${inserted_coins}")
            if check_transaction(inserted_coins,cost):
                make_coffee(user_coffee)
                print(f"here is your {user_coffee} ☕🍵 Enjoy!")
            else : 
                print("sorry! there is not enough money")
        else :
            print("sorry! there is not enough resource. ")    
                