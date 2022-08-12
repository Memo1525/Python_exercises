#if we don
from types import MethodType
class Program:
    language = 'python'
    def say_hello():
        print(f'hello from {Program.language}')


#print(Program.__dict__)
#Program.say_hello()
instance1 = Program()

#when we make instaciation the objects take the atributes of the class but you can create new atributes in the instanciation
#no matter if they have the same name because it's going to take this first if the ptogram didn`` found anything basically search in the class

instance1.bank = "Acme savings & loans"

print(instance1.bank)
print(type(instance1.__dict__))

del instance1.bank
#print(instance1.bank)

#__self__ -> the instance the method is boun to

#__func__ -> the original function (defined in the class)

#callling obj.method(args) -> method.__func__(method.__self__,args)

#why we use self , because whiout self we can use the methods in the instances but yes on the class itself

class Myclass:
    language ='Python'

    def say_hello(self,name):
        return f"Helllo {name} I am a {self.language}"

#class namespace instance namespace


#Function Attributes
class Personp:
    def say_hello(self):
        print("hello")
p = Personp()

#method a function that is bound to a object py
print(type(p.say_hello))

class person2:
    def set_name(self,new_name):
        self.name = new_name
p2 = person2()

class Person():
    def say_hello(self):
        print(f'say{self} says hello')

#function that are defined in the class are transformed in methods when we instanciate
#we need to make sure that always have self by convention we called self


# ----------------- INitializer or constructor ----------------------

class myClass:
    def __init__(self,version):
        self.version = version

#creating attributes at running time
class Person3():
    pass
p1 = Person3()
p2 = Person3()

p1.name = 'Alex'
print(p1.__dict__)
p1.say_hello = lambda : 'Hello'



from types import  MethodType
class Person34:
    def __init__(self, name):
        self.name = name

    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func , self))
    def do_work(self):
        do_work_method = getattr(self, '_do_work',None)

        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('You must first register a do_work method ')


#y esto lo podemos utilizar de la siguiente manera creando un metodo y  pasandoselo a una instancia
#necesito instanciar el objeto del teacher
english_teacher = Person34('Eric')
def work_english(self):
    return f'self{self.name} will analize Hamlet today'
english_teacher.register_do_work(work_english)


#como crear una metodo en una instancia y no en la clase
p1.say_hello = MethodType(lambda self: f'{self.name} says hello' ,p2)

#como crearlo solo en la clase
Person.hacer_perros = lambda : 'Hello'

print(Person.__dict__)





#si me dicen creame un ejemplito basico de un handling exceptions -> le daria algo asi

while True:
    try:
        x = int(input("Please enter a number : "))
        break
    except ValueError:
        print("That is invalid , :( ")































