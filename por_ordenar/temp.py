list=[7, 9, 7, 13, 11, 11, 7, 13, 9, 9, 9, 11, 9, 5, 3, 5, 13]
dictt={}
for element in list:
    if element not in dictt:
        dictt[element]=1
    else:
        dictt[element]+=1
print(dictt)

lista=[i for i in range(10)]
diccio={}
for element in lista:
    if element not in diccio:
        diccio[element]=1
    else:
        diccio[element]+=1
print(diccio)