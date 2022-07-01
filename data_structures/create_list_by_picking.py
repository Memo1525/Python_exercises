l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3=[]
for i in range(1,len(l1)):
    if i%2==1:
       l3.append(l1[i])

for i in range(0,len(l2)):
    if i%2==0:
       l3.append(l2[i])
print(l3)      

#----------------
odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]

#this is fairly a better solution 
