#if the s1 is container in s2 True otherwise False
s1 = "Ynx"
s2 = "PYnative"

def balance(s1,s2):
# corner case
    if  len(s1) > len(s2):
        return("S1 must be shorter than s2")
    for i in s1:
        if i in s2:
            continue
        else:
            return("Not balanced")
    return True

print(balance(s1,s2))
#this is partially correct because we only check the string combinatiog

#solution provided by the book 
def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)