string = 'ABCDCDC'
substring = 'CDC'
contador=0
contador2=0
for i in range(len(string)):
    if (string[i:].startswith(substring)):
        contador+=1
print(contador)

for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        contador2+=1
print(contador2)

for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        contador2+=1
print(contador2)
