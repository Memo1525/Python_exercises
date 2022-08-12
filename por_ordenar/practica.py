#dame la letra con el mayores  repeticiones  del siguiente string
s="colalocaaa"
lista=[]
for i in s:
    lista.append(([s.count(i),i]))
print(max(lista))

mapa={}
contador=1
for letra in s:
    if letra in mapa:
        mapa[letra]+=1
    else:
        mapa[letra]=1

print(mapa)
print(max(mapa.items(),key=lambda x: x[1]))
