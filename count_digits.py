# 75869, so the output should be 5.
# one way is to convert to string 
number=75869
counter=0
while number !=0:
    number //= 10
    print(number)
    counter+=1
print(counter)

nn=112
print(nn//10)