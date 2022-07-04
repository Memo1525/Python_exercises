objetos = {
    '1': ['A', 'B', 'C'],
    '2': ['A', 'M', 'Y'],
    '3': ['A', 'B', 'D'],
    '4': ['D', 'X', 'C']
}
def sistema_experto_v3(objetos):
    datos = list(input("Ingresa los hechos iniciales separados por un espacio: ").upper().split())
    for i in range(len(objetos)+1):
        if i > 0:
            if objetos[str(i)] == datos:
                return f"tu objeto es el {i}"
    return f"El objeto no existe"
print(sistema_experto_v3(objetos))


'''

s = "   fly me   to   the moon  "
print(s.split()[-1])
lista=['lola','lulu','maria']
print("".join(lista))

#first non repeated character
l="hoola"
for i in range(len(s)):
    if i
'''