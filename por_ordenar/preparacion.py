#como hacer un testeo de una manera fancy
'''
try:
    p.set_name(100)
except ValueError as ex:
    print(ex)
'''
# esto es un string muy padre para probarlo
"".join() #hace un string a partir de un iterable
map(lambda x:x**x,[1,2,3,4,5]) #le añade cosas  a un iterable lo hace crecer o aumnentar o algo hace
#un ejemplo muy bueno y muy util con filter es el siguiente
numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers=filter(lambda x : (x%2==0),numbers)
even_numbers2=[i for i in numbers if i % 2 ==0 ]
print(string.strip('an')) # tambien puedes especificar algunos parametros


filter()
.split() #esta hace un string una lista , se le puede añadir un maxsplit+1 print(grocery.split(', ', 1))
strip() # Leading and trailing whitespaces are removed print(string.strip())


#---------------------------  Fibonacci with recursion -------------------------
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

#--------------solucion matematica en fibonacci -----------------
def sum(n):
    return n * (n+1) /2
#------------------  StartsWIth---------------
string = 'ABCDCDC'
substring = 'CDC'
contador=0
for i in range(len(string)):
    if (string[i:].startswith(substring)): #if (string[i:].startswith(substring)): if (string[i:].startswith(substring))
        contador+=1
for i in range(len(string)):
    if (string[i:].startswith(substring)):
        contador+=1

#-------------------------- longest substring -----------------------
    def longestPalindrome(self, s):
        def check_palin(s):  # helper function
            return (s == s[::-1])

        for lenght in range(len(s), 0, -1):  # anita
            for start_index in range(0, len(s) + 1 - lenght):  # checa todos y va disminuyendo 4
                if check_palin(s[start_index:(start_index + lenght)]):
                    return s[start_index:(start_index + lenght)]

#-------------------------------------------------
#devolver la letra con mayores ocurrencias de un strig
s="colalocaaa"
lista=[]
for i in s:
    lista.append(([s.count(i),i]))
print(max(lista))

s="something"
for i in s :
    lista.append([s.count(i),i])
print(max(lista))


mapa={}
contador=1
for letra in s:
    if letra in mapa:
        mapa[letra]+=1
    else:
        mapa[letra]=1
#--------------------------------------------------
#aqui imprimimos los caracteres faltantes en un string
def missingCharacters(s):
    todo = '0123456789abcdefghijklmnopqrstuvwxyz'
    nuevo = []
    for i in range(len(todo)):
        if todo[i] not in s:
            nuevo.append(todo[i])
    return "".join(nuevo)
#------------------------------------------------
#para saber si es un pangram
def isPangram(pangram):
    return len(set(list(pangram.lower())))==26
#-----------------------------------------------
#pangram con la funcion de
def isPangram2(pangram):
    c=0
    s=set()
    for xx in pangram.lower():
        x = ord(xx)-ord('a')
        if x not in s and x>=0 and x<26:
            c+=1
            s.add(x)
            if c==26:
                break
    return c==26
#-------------------------------------------------
def wordBreak(wordlist,word):
    if word == '':
        return True
    else:
        wordlen = len(word)
        x=[(word[::i] in wordlist) and wordBreak(wordlist, word[i:]) for i in range(1,wordlen+1)]
        print(x)
        return any(x) #devuelve true si alguno de la lista es verdadero
print(wordBreak(["ibm","i","love","and","world"],"iloveibmandword")) #esta funcion hace esto

#---------------------------------------------------
#devolver el area de un triangulo con coordenadas dadas
Triange_Area = abs((0.5)*(x[0]*(y[1]-y[2])+x[1]*(y[2]-y[0])+x[2]*(y[0]-y[1])))
#con esto imprimimos todo el perro string cosa por cosa
for j in range(len(string) - 2):
    for i in range(j + 1, len(string) - 1):
        for k in range(j + 2, len(string)):
            print(string[j] + string[i] + string[k])
            if string[j] + string[i] + string[k] == sub_string:
                contador += 1

#swap de caracteres entre mayusculas y minusculas
def swap_case(s):
        return s.swapcase()
#-------------------------------------
#hacer el swap sin la funcion
for letter in s:
    if letter == letter.upper():
                result += letter.lower()
    else:
                result += letter.upper()
    return result

#first non-repeated-character
s='vivamexico'

def fnrc(str):
    for i in s:
        if s.count(i)==1:
            return i
print(fnrc(s))
#ordenar elementos en un diccionario
l={c:v for c,v in sorted(x.items(),key=lambda x:x[1])}
l={c:v for c,v in sorted(x.items()),key=lambda x:x[1]}
d={c:v for c,v in sorted(x.items(),key=lambda  x:x[1])}
sorted(x.items(),key=lambda  x:x[1])


#si te dicen de un diccinario dame la clave mayor

print(max(dict.values()))
l={c:v for c,v in sorted(dict.items(),key=lambda x:x[1])}

#----------------------------------
def minion_game(string):
    # your code goes here
    # utilizar funcion starswith
    contadorVoc=0
    contadorCon=0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            contadorVoc+=len(string)-i
        else:
            contadorCon+=len(string)-i
    if contadorVoc > contadorCon:
        print(f"KEVIN {contadorVoc}")
        return f"KEVIN {contadorVoc}"
    else:
        print(f"STUART {contadorCon}")
        return f"STUART {contadorCon}"
#-----------------------------------------
def climbStairs(self, n: int) -> int:
    path = {1: 1, 2: 2, 3: 3}
    for x in range(4, n + 1):
        path[x] = path[x - 1] + path[x - 2]
    return (path[n])

string='asdf'
diccionario={}
for i in range(len(string)):
    if string[i] not in diccionario.keys():
        diccionario[i]=1
    else:
        diccionario[i] +=1



