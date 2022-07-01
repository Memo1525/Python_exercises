str1 = "Emma25 is Data scientist50 and AI Expert"

lista=str1.split()
res=[]
for i in range(len(lista)):
    if lista[i][-1].isnumeric():
        print(lista[i])


for item in lista:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

for i in res:
    print(i)        