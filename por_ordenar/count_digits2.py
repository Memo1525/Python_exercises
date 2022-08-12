number = 75689
count=0

#para contar sin ingu otro auxiliar es lo sigiente 
while number !=0:
    number //=10
    count +=1
print(count) 
    
    
#reminder prime numbers

start=25
end = 50 
for num in range(start,end+1): #uno para checar solo el rango dado 
    #if number is less than or equal to 1, it is not prime 
    if num > 1:
        for i in range(2, num): # otro para recoger todo hasta ese punto 
            #check factors
            if num % i == 0:
                break
        else:
            print(num)
            
#fibonacci
num0=0
num1=1
for i in range(8):
    sumatoria=num0 + num1
    if i == 0:
        print(num0)
        print(num1)
    num0=num1
    num1=sumatoria
   
    print(sumatoria )
    
       
fibonaci=[0,1]
for i in range(1,9):
    suma=fibonaci[i]+fibonaci[i-1]
    fibonaci.append(suma)
print(fibonaci)