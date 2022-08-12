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

#valdra la pena buscar algun metodo de recursion o mas eficiente



def factorial(number):
    facto=1
    if number < 0:
        return 'Must be greater than  0 '
    elif number==0:
        return 'The factorial of 0 is 1 '
    else:
        for i in range(1,number+1):
            facto *=i
        return facto
    
print(factorial(5))

#reverese a given integer number]
given=76542
reverse_number =0 #this is the uax variable 
while num > 0:
    reminder = num %10 #this will give us the last number 
    reverse_number *= 10 + reminder 
    num //=10 #this will reduce the number by one by one 
    
    reminder =num%10