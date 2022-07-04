'''


def minion_game(string):
    # your code goes here
    # utilizar funcion starswith
    contadorVoc=0
    contadorCon=0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            contadorVoc+=len(string)-i
        else:
            contadorCon+=len(string)-i
    if contadorVoc > contadorCon:
        print(f"KEVIN {contadorVoc}")
        return f"KEVIN {contadorVoc}"
    else:
        print(f"STUART {contadorCon}")
        return f"STUART {contadorCon}"


print(minion_game("BANANA"))

'''
#como hacer que un diccionario itere sobre una lista y me devuelva el numero de
#elementos en un mapa o algo asi
'''

cadena="hola000"
diccionario={}
for i in range(len(cadena)):
    if cadena[i] not in diccionario.keys():
        diccionario[cadena[i]]=1
    else:
        diccionario[cadena[i]]+=1
#max_key = max(stats, key=lambda key: stats[key])
#print(max(diccionario, key=lambda key: diccionario[key]))
#val = max(verse_dict.items(), key=obtener_valor)[0]
print(max(diccionario.items(),key=lambda x: x[1]))
'''

cadena='hola0000'
diccio={}
for i in range(len(cadena)):
    if cadena[i] not in diccio.keys():
        diccio[cadena[i]]=1
    else:
        diccio[cadena[i]]+=1
print(max(diccio.items(), key=lambda x: x[1]))

#en una situacion totalmente hipotetica necesito ordenar un diccionario por valor
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}


l={c:v for c,v in sorted(x.items(),key=lambda x:x[1])}
print(l)