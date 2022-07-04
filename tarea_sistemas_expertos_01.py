objetos={
'1':{'A','B','C'},
'2':{'A','M','Y'},
'3':{'A','B','D'},
'4':{'D','X','C'}
}
inferencia=[]
i=-1
datos=['A','B','C','A','M','Y','A','B','D','D','X','C']
while True:
    i+=1
    if i >= len(datos):
        break
    if input(f"Tiene {datos[i]}: ") == 'si':
            inferencia.append(datos[i])
    if {'A', 'B', 'C'} ==set(inferencia):
        break
    if {'A', 'M', 'Y'} == set(inferencia):
        break
    if {'A', 'B', 'D'}  == set(inferencia):
        break
    if {'D', 'X', 'C'} == set(inferencia):
        break


for i in range(len(objetos)):
   if  objetos.get(str(i)) == set(inferencia):
       print(f"Tu objeto es el {i}")