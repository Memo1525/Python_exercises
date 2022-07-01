str1 = "Apple"
mapa={}

for i in str1:
    if i not in mapa:
        mapa[i]=1
    else:
        mapa[i]+=1

print(mapa)    