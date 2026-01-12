def is_prime(number):
    x=1
    number_of_divisible=0
    for x in range(number):
        x+=1
        if number % x==0:
            number_of_divisible+=1
    if number_of_divisible ==1:
        return False   
    elif number_of_divisible> 2:
        return False
    else :
        return True
    

print(is_prime(1))