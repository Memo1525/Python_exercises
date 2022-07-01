s1 = "America"
s2 = "Japan"

def new_string(s1,s2):
    midle=len(s1)//2
    midle2=len(s2)//2
    
    si=s1[:1:]
    sf=si+s2[:1:]
    sf = sf + s1[midle:midle+1]
    sf = sf + s2[midle2:midle+1]
    sf += s1[-1]
    sf += s2[-1]
    return(sf)

print(new_string(s1,s2))
    
