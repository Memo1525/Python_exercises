#__repr__ is for developers
# is called when we use repr()
#__str__ is used by str() and print()
#repr is called on the print method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        print('__repr__ called')
        return f"Person(name={}, age={self.age})"

    def __str__(self):
        print('__str__called')
        return self.name


#every object has a repr method because it inherits to the base class

p = Person('python',30)

print(f"the person is {p}")

__add__ = +

__sub__ = -

__mul__ = *

__truediv__ = /

__floordiv__ = //

__mod__ = %

__pow__ = **

__matmul__ = @ #this was added for matrix multiplication (only for numpy)


#reflected Operators
__radd__ = +

__rsub__ = -

__rmul__ = *

__rtruediv__ = /

__rfloordiv__ = //

__rmod__ = %

__rpow__ = **




# in place operators
__iadd__ +=

__isub__ -=

__imul__ *=

__itruediv__ /=

__ifloordiv__ //=

__imod__ %=

__ipow__ **=

#unary operators
__neg__ = -a
__pos__ = +a
__abs__ = abs(a)




