str1 = "Welcome to USA. usa awesome, isn't it?"
#count the word usa 
contador=0
str1 = str1.replace(" " , "")
for i in range(0,len(str1),1):
    l=str1[i:i+3]
    if "usa" in l:
        contador+=1
    if 'USA' in l:
        contador+=1
        
print(contador)

#solution provided by the book 
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)

        
    
    
    