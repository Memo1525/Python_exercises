list1 = [54, 44, 27, 79, 91, 41]

print(list1)
x=list1.pop(4)
list1.insert(2,x) #position,element 
list1.append(x)
print(list1)




#remove method 
#if we put the number like parameter it 
#will delete the number 
#like list1.remove(91) it will remove 91 

#methods to work with lists 
'''
del function helps to delete the list variable from code.
pop function helps to delete the individual element according to positioning of the list. Return the position value.
remove function helps to delete the first occurrence of the number or string mentioned in its arguments.
Clear function clear the all elements present in the list without delete its variable.
#Program: 
>>> a=[1,2,3,4,5,"sahil"] 
>>> a.pop(0)# delete element at position 0 
1 
>>> a 
[2, 3, 4, 5, 'sahil'] 
>>> a.remove(2)# delete element 2 that present at 0 position 
>>> a 
[3, 4, 5, 'sahil'] 
>>> del a[1:3] # delete multiple elements from list at position 1 to 2 
>>> a 
[3, 'sahil'] 
>>> a.clear()# clear the list 
>>> a 
[] 
'''