#str1, str2, str3 = input("Enter three string").split()
str1, str2, str3 = input("Enter three string: ").split() 
str11,str22,str33 = input("Enter three string: ").split()

#check is a file is empty or not 
import os 
size = os.stat("test.txt").st_size
if size == 0:
    print(False)
    