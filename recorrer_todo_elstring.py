string="elweropalama"
#contador=0
substring='wer' #this may vary according to the excercise
for j in range(len(string) - 2):
    for i in range(j + 1, len(string) - 1):
        for k in range(j + 2, len(string)):
            print(string[j] + string[i] + string[k])
            if string[j] + string[i] + string[k] == substring:
                pass
                #contador += 1
#print(contador)

contador=0
for j in range(len(string)-2):
    for j in range(i+1,len(string)-1):
        for k in range(j+1,len(string)):
            if string[i]+string[j]+string[k] == substring:
                contador+=1
print(contador)