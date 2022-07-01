import string
str1 = '/*Jon is @developer & musician!!'
for char  in string.punctuation:
    str1 =str1.replace(char,'#')
    str1=str1.replace(char,'#')
print(str1)

print(string.punctuation)