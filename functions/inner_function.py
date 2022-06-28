def outer_fun(a,b):
    square = a ** 2
    def inner2(a,b):
        return a+b
    add = inner2(a,b)
    
    return add+ 5 

result = outer_fun(5,10)
print(result)
