

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

lista3=list1[2::2]
temp=list2[0::2]
lista3.extend(temp)
print(lista3)

odd=[number for number in list1 if number %2==1]
even=[number for number in list2 if number %2==0]

odd.extend(even)
print(odd.extend(even))