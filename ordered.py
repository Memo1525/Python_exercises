def missingCharacters(s):
    todo = '0123456789abcdefghijklmnopqrstuvwxyz'
    nuevo = []
    for i in range(len(todo)):
        if todo[i] not in s:
            nuevo.append(todo[i])
    return "".join(nuevo)

print(missingCharacters('12345689abcdefghijklmnopqrstuvwxyz'))