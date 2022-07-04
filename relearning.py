datos = []
scores = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        datos.append([name, score])
        scores.append(score)

datosor = sorted(datos, key=lambda x: x[0] ,reverse=True)
datosor = sorted(datos,key=lambda x:x[0],reverse=True)
second = sorted(list(set(scores)))[1]

print(datosor)
print(second)
for x in range(len(datosor)):
        if second == datosor[x][1]:
            print(datosor[x][0])