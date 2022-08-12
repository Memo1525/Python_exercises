def checkInclusion(s1: str, s2: str) -> bool:
        partial=[]
        partial.append(s1[0])
        for i in range(1,len(s1)):
            for j in reversed(range(len(partial))):
                curr = partial.pop(j)
                for k in range(len(curr)+1):
                    partial.append(curr[:k]+s1[i]+curr[k:])
        print(partial)
        for i in partial:
            if i in s2:
                return True
        return False

print(checkInclusion('adc','dcda'))

#window slicing technique
def Count(cadena , sub):
    index=[]
    for i in range(len(cadena)):
        if cadena[i:i+len(sub)]==sub: #basically this is the window slicing technique
            index.append(i)