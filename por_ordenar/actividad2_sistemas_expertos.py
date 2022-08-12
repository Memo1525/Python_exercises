# utilizando encadenamiento hacia atras
# el objeto no debe de preguntar lo que ya pregunto con anterioridad
# decidir el tipo de objeto con el que se empezara a agregar los datos en este caso un diccionario de listas
objetos = {
    '1': ['A', 'B', 'C'],
    '2': ['A', 'M', 'Y'],
    '3': ['D', 'X', 'C'],
    '4': ['A', 'B', 'D']
}
tiene = []
no_tiene = []
def sistema_experto_ver2(objetos,tiene,no_tiene): #diccionario , lista vacia
    for i in range(len(objetos)):
        for j in range(len(objetos[str(i+1)])):
            if objetos[str(i+1)][j] not in tiene and objetos[str(i+1)][j] not in no_tiene  :
                if input(f'Tiene {objetos[str(i+1)][j]} : ') =='si':
                    tiene.append(objetos[str(i+1)][j])
                else:
                    no_tiene.append(objetos[str(i+1)][j])

        if sorted(tiene) == sorted(objetos[str(i+1)]):
            return ( f'tu objeto es el objeto {i+1}')
print(sistema_experto_ver2(objetos,tiene, no_tiene))



