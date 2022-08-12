
#if len(c)<=4: #condicion 1
 #   pass
#else:
 #   print('esta no es')

s="id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n,17,Betty,28,F,15,7"
c='room'
lista2=s.split(",")
saltos_de_linea=s.count('\n')
lista_final = []
lista_temporal=[]
for i in range(len(s)):
    if '\n' in s[i]:
        if len(lista_temporal)==0:
            l = i
            lista_temporal=s[:i]
            lista_final.append(lista_temporal)
            print(l)
        else:
            print(lista_final.append(s[l:i]))

print(lista_final)


print(s.count('\n'))


'''

print(len(c))
if len(c)<5:
    print( c in lista2)
    print(lista2.index(c)+1)
    print( p in lista2)
else:
    pass
'''