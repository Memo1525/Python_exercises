# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
fibonacci= [0,1]
for i in range(11):
    suma=fibonacci[i]+fibonacci[i+1]
    fibonacci.append(suma)
    if len(fibonacci)==10:
        break
print(fibonacci)

#solution provided by the book
# first two numbers

#this solution is complex at least for me 
#because the variable interchanging is challenging 
num1, num2 = 0, 1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num1, end="  ") #print 0 
    # add last two numbers to get next number
    res = num1 + num2 #res =1 

    # update values
    num1 = num2 #num1 = 1 
    num2 = res # num2=  1 
    
    #the porpouse of fibonacci is to go ahead with one variable to catch the sum 
    
    
    here i need to look the recursive one 