num=11
temp=0
for i in range(11):
    temp+=i
print(temp)

print(sum(range(num)))
#la funcion sum es muy interesante
#ya que solo le pasas un iterable y te devuelve la suma de todos los valres 
#ejemplo sum(range(11)) = 55 

for i in range(1,11):
    print(i*2)