number= 76542
lnumeros=[]
for i in range(5):
    temp=number%10
    lnumeros.append(temp)
    number//=10
#my approach 
print(lnumeros)

print(str(number)[::-1])
    
#provided by the book 
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder #here is the important part were multiplicates by 10 + reminder so we don't need a list  !marvelous!
    num = num // 10
print("Revere Number ", reverse_number)
    
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list[1::2])    