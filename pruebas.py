#longest palindromic substring
#tratar los casos esquina
#subir algun tipo de codigo
#use the white board for 5 minutes in order to think a solution
#whren there is no a palindrom but the string is larger than 1 the result is 1
#cuando en uno de los problemas no encuentre solucion lo que debere de hacer sera lo siguiente checar en los problemas previos y ver las discuciones
#in some harder problems maybe we need a helper function


def longestPalindrome(self,s):
        def check_palin(s): #helper function
            return (s == s[::-1])
        for lenght in range(len(s),0,-1):   #anita
            for start_index in range (0,len(s)+1-lenght): #checa todos y va disminuyendo 4
                if check_palin(s[start_index:(start_index+lenght)]):
                    return s[start_index:(start_index+lenght)]
        # check all substrings
        # nota la siguiente solucion es de fuerza bruta

if s.count(i)
lista=["a","b","c","d"]

print(lista[::-1])

cadena="anitalavalatina"
print(cadena[::-1])
