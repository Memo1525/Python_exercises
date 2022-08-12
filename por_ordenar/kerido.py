s='hooolah'
def fnrc(str):
    for i in s:
        if s.count(i)==1:
            return i
print(fnrc(s))

def fnrc(str):
    for i in s:
        if s.count(i)==1:
            return i
print(fnrc(s))
#multiples non repeative characters
caracteres=[]
def fnrc2(str):
    for i in s:
        if s.count(i)==1:
            caracteres.append(i)
    return caracteres

def fnrc2(str):
    for i in s:
        if s.count(i)==1:
            pass

lista=["l","q"]
diccion={'q':'respuesta'}


# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
dict_comprenhension = {}
numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers=filter(lambda x : (x%2==0),numbers)
even_numbers2=[i for i in numbers if i % 2 ==0 ]
print(list(even_numbers))
print(even_numbers2)