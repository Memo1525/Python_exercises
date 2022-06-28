#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10
def recursive(num):
    if num: #this is the base case
        return num + recursive(num-1)
    else:
        return 0 
res = recursive(10)
print(res)

###\
    # is posible to rename a function using only the = symbol
    
def display_student(name,age):
    print(namne,age)

showStudent = display_student

showStudent("Emma", 26)