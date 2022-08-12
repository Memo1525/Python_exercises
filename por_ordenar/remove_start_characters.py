#Write a program to remove characters from a string starting from zero up to n and return a new string.
string="PYNATIVE"
user=int(input())
def remove_start_char(string,user):
    if user > len(string):
        return("ingresa un numero menor a la longitud de la cadena ")
    return (string[user:])

print(remove_start_char(string,user))