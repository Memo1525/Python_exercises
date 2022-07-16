#Write a program to check if the given number is a palindrome number.
from audioop import reverse


number=int(input())
cadena=str(number)
if cadena == cadena[::-1]:
    print(True)
else:    
    print (False)
    
##book solution 
def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
        
        
        
    reverse_num=0     
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num*10) + reminder 
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)