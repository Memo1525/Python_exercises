sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
mapa={}
for i in sample_list:
    if i not in mapa:
        mapa[i]=1
    else:
        mapa[i]+=1
print(mapa)
        