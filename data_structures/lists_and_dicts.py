sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
roll_number2=[47, 64, 69, 37, 76, 83, 95, 97]
nueva_lista=[]
for i in roll_number2:
    if i  in sample_dict.values():
         nueva_lista.append(i)
 

         

print(nueva_lista)