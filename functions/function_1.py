def age(num,name):
    return f"my name is {name} and  my age is {num}"

print(age(22,'brian '))

#functions with variable arguments
#to create functions that take n number of positional arguments
#we use *args as a parameter all these values are represented in a tuple 
def func(*args):
    print(args)
print(func(10,20,30))