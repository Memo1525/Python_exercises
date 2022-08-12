#check if a string is pangram
def isPangram(pangram):
    return len((set(list(pangram.lower()))))==26

def isPangram2(pangram):
    return len(set(list(pangram.lower())))==26

#que tal si me ponen simbolos raros
#return len(set(filter(lambda x: ord(x)>= ord('a') and ord(x)<= ord('z')),list(pangram.lower()))))==26

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

#here it is a another program

def checkGrammar(inputString1):
    i = inputString1
    print(i)
    if i == '{}':
        return "Set"
    elif i=='{,}':
        return "Set"
    elif i[0]=='{' and i[-1]=='}':
        return "Set"
    elif i == '{,,}':
        return "NotSet"
    else:
        return "NotSet"

# in this you need to figure out where the string is constructed from this set of words
def wordBreak(wordlist,word):
    if word == '':
        return True
    else:
        wordlen = len(word)
        x=[(word[::i] in wordlist) and wordBreak(wordlist, word[i:]) for i in range(1,wordlen+1)]
        print(x)
        return any(x) #devuelve true si alguno de la lista es verdadero
print(wordBreak(["ibm","i","love","and","world"],"iloveibmandword"))

'''

i loveibmandworld "True"
  love  ibmandworld "True"
        ibm andworld "True"
            and world "True"
                world "True"
'''
#variation of the wordbreak
def wordBreak(wordlist,word):
    if word == '':
        return True
    else:
        wordlen = len(word)
        res = False
        for i in range (1, wordlen+1):
            if (word[::i] in wordlist) and wordBreak(wordlist,word[i:]):
                return True
            return False




#lower_pangram='qwertyuioasdfghjklpzxcvbnmZZ'
#prueba=lower_pangram.lower()
#print(type(prueba))
#print(prueba)
print(isPangram(input()))

#what if we need lowercases

#return (len(set(filter(lambda x: ord(x)>=ord('a')))))