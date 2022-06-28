#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
s1 = "Ault"
s2 = "Kelly"

def append_middle(s1,s2):
    mi = int(len(s1)/2)
    x= s1[:mi:]
    x+=s2
    x= x + s1[mi:]
    return x

    mi = int(len(s1)/2)
    x= s1[:mi:] # here we put the start 
    x+=s2 # here we put the second word 
    x = x + s1[mi:] #append the final part to the word 
    

print(append_middle(s1,s2))