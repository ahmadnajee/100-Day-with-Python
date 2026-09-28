

with open("./Dy 26/file1.txt", "r") as file:    
    file1 = file.readlines()
    
    
with open("./Dy 26/file2.txt", "r") as file:
    file2= file.readlines()
   

result = [int(num) for num in file1 if num in file2]

print(result)