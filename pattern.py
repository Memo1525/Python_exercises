"""
Print the following 
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
#the dump way is with 5 prints
#docle for loop 


for i in range(6):
    for j in range(i):
        print(i,end="")
    print("\n")
    