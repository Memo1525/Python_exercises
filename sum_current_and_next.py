#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
for i in range(0,10):
    if i == 0:
        print( f"Current Number {i} Previous Number {i}  Sum: {i}")
    else:
       print( f"Current Number {i} Previous Number {i-1}  Sum: {i+i-1}") 
    
#Solucion provista por el libro 
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    # modify previous number
    # set it to the current number
    previous_num = i
    
    #cosas interesantes 
    # para guardar una varible i en una variable solo la asigna al final y con eso quedaria que chido 
    