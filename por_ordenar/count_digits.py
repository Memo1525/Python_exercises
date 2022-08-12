# 75869, so the output should be 5.
# one way is to convert to string 
number=75869
#counter=0
#while number !=0:
#   number //= 10
#    print(number)
#    counter+=1
#print(counter)

counter=0
#como contar los digitos 
while number !=0:
    print(number%10) #con el modulo obtienes el numero sin el ultimo digito 
    number //=10 #con esto se elimina el ultimo digito 
    counter+=1 #se cuenta la eliminacion 
    
print(counter)
