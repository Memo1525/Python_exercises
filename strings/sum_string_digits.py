from curses.ascii import isdigit


str1 = "PYnative29@#8496"
#expected output 
#Sum is: 38 Average is  6.333333333333333
contador=0
average=0
for i in str1:
    if i.isdigit():
        contador+=int(i)
        average+=1

print(contador)
print(contador/average)
        


        