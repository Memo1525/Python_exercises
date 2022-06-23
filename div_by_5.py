#Iterate the given list of numbers and print only those numbers which are divisible by 5
#with for loop
lista=[10, 20, 33, 46, 55]
for i in lista:
    if i % 5 ==0:
        print(i)

#with list comprenhension 
#[number for number in iterable condition ]
#[expression for item in list]
lista_c=[x for x in lista  if x % 5 ==0]
print(lista_c)

#Write a program to find how many times substring “Emma” appears in the given string.
#this is my approach 
string= "Emma is good developer. Emma is a writer"
print(string.count("Emma"))

#approach without the string method 
count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count
#the important part 
# statement[i:i+4] =='Emma'"
