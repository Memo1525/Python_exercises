#mi propia solucion a fibonacci

def ownFibo(n):
    if n  < 0:
        return "must be non-negative num"
    if n ==1:
        return 1
    base={1:1,2:2,3:3}
    for i in range(3,n+1):
        base[i]=base[i-1]+base[i-2]
    return base[n]

def otherFibo(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    else:
        return (otherFibo(n-1)+otherFibo(n-2))

print(otherFibo(10))
print(ownFibo(10))


def climbStairs(self, n: int) -> int:
    path = {1: 1, 2: 2, 3: 3}
    for x in range(4, n + 1):
        path[x] = path[x - 1] + path[x - 2]
    return (path[n])

def climbStairs2(n):
    path = {1:1,2:2,3:3}
    for x in range(4,n+1):
        path[x] = path[x-1] + path[x - 2]
    return (path[n])

def shortStairs(n):
    if n % 2 == 0:
        
# sorted(iterable, key=None, reverse=False)
def addTwoNumbers(l1,l2) :
        cadena1 = "".join(l1)
        cadena2 = "".join(l2)
        sumatoria = int(cadena1)+int(cadena2)
        return str(sumatoria[::-1])
#print(addTwoNumbers([2,3,4], [4,1,7]))
l1=[4,1,7]
print(l1[::-1])
print(str(l1))

#recordar el count importante checar el count ver un video antes de que se termine el dia
class Myclass:
    def __init__(self):
        self._language = language

    def get_language(self):
        return self._language
    def set_language(self, value):
        self._language = value
    language = property(fget=get_language, fset=set_language) #esto nos permite mas control dentro de la clase y ademas nos ayuda a establecer parametros

    

