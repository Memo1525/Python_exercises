#REQUISITOS PARA LA RECURSIVIDAD QUE SE REPITA VARIAS VECES EL

string = 'ABCDCDC'
substring = 'CDC'
contador=0
for i in range(len(string)):
    if (string[i:].startswith(substring)):
        contador+=1
for i in range(len(string)):
    if (string[i:].startswith(substring)):
        contador+=1

#print(contador) aqui muestra el resultado



def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)



# Driver Program
for i in range(11):
    print(Fibonacci(i))

print(Fibonacci(10))

# solucion iterativa
def sum(n):
    result=0
    for i in range(n+1):
        result +=i
    return result
print(sum(10))


#generalize the pattern

def sum(n):
    return n * (n+1) /2

def suma_rec(n):
    if n==0:
        return 0
    else:
        return n + suma_rec(n-1)

print(suma_rec(10))
