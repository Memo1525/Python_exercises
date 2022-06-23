#constraints
# div by five
# if is greater than 150 skip
# greater than 500 stop 

numbers = [12, 75, 150, 180, 145, 525, 50]
new_list=[number for number in numbers if number <= 150 and number % 5 == 0  ]
print(new_list)
newlist2=[]

for i in numbers:
    if i >= 500:
        break
    if i > 150:
        continue
    if i % 5 == 0:
        newlist2.append(i)
print(newlist2)