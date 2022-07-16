#number=int(input())
#chain=str(number)
#print(str(number)[::-1],end="")

#solution provided by the book 
number = 7536
cnumber=number
contador=0
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    contador += number
    print(digit, end=" ")