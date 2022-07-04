#first non-repeated-character
s='vivamexico'

def fnrc(str):
    for i in s:
        if s.count(i)==1:
            return i
print(fnrc(s))



#first non repeated character
def fsnonrepeated(s):
    for i in s:
        if s.count(i)==1:
            return i
print(fsnonrepeated(s))

def fsnrc2(string):
    mapa={}
    for i in s:
        if i not in mapa:
            mapa[i]=1
        else:
            mapa[i]+=1
    for key,value in mapa.items():
        if 1 == value:
            return key
print(fsnrc2(s))


#---------------------------------------

s='vivamexico'

def fnrc(str):
    for i in s:
        if s.count(i)==1:
            return i
print(fnrc(s))

def fnrc(string):
    for i in s:
        if s.count(i)==1:
            return i 
print(fnrc(s))

def own(s):
    mapa={}
    for i in s:
        if i in mapa:
            mapa[i]+=1
        else:
            mapa[i]=1
    for key, value in mapa.items():
        if value ==1:
            return key
print(own(s))
        