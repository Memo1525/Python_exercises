s='deeedbbcccbdaa'
k=2
mapa = {}
for element in range(len(s)):
        if s[element] in mapa:
            mapa[s[element]] += 1
        else:
            mapa[s[element]] = 1

lista_de_datos=[]
for new_k , new_v in mapa.items():
    lista_de_datos.append([new_k,new_v])


