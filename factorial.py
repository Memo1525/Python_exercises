#factorial 
num=5 
facto=1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(num,0,-1):
        facto *= i


print(facto)    
