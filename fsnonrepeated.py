s='lacolalocatrarezedsqwrtrwredzhvcmjhgliuresajvv'
def fsnonrepeated(s):
    for i in s:
        if s.count(i)==1:
            return i
print(fsnonrepeated(s))

