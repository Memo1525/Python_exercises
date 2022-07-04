objeto1=['g','k','h','a','e','l','k','b']
objeto2=['j','g','e','f']
objeto3=['j','h','a','d','e','c']

dato1,dato2=input().split()
def se4(dato1,dato2):
    contador1, contador2, contador3 = 0, 0, 0
    for i in range(len(objeto1)):
        if objeto1[i]==dato1:
            contador1+=1
        if objeto1[i]==dato2:
            contador1+=1
        if contador1==2:
            return "tu objeto es el numero 1"
    for i in range(len(objeto2)):
        if objeto2[i]==dato1:
            contador2+=1
        if objeto2[i]==dato2:
            contador2+=1
        if contador2==2:
            return "tu objeto es el numero 2"
    for i in range(len(objeto3)):
        if objeto3[i]==dato1:
            contador3+=1
        if objeto3[i]==dato2:
            contador3+=1
        if contador3==2:
            return "tu objeto es el numero 3"


print(se4(dato1,dato2))

