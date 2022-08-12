#Write a program to accept a string from the user and display characters that are present at an even index number.
user=input(str())

for i in range(len(user )):
    if i % 2 == 0:
        print(user[i])
#the above solution is my solution 
#but here are another solutions
#one is using the string 
#solucion 1 
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])

#this is interesant because is using (range(start,stop,step))

#this is with list slicing 
user=input(str())
x = list(user)
for i in x[0::2]:
    print(i)

