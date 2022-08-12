class Person:
    """This is a totally useless message """
    def __init__(self, name):
        self._name = name#private but for make more secure we can make set_name

    def get_name(self):
        return self._name
    def set_name(self , value):
        if isinstance(value, str) and len(value.strip()) > 0: #aqui se debe de añadir una validacion ya que de no ser asi no tendria mucho sentido
            self.nmae = value.strip()
        else:
            raise ValueError('name must be non-empty')
    def del_name(self):
        del self._name
    name = property(fget=get_name, fset=set_name, fdel=del_name)



class Myclass:
    def __init__(self, language):
        self._language = language

    @property
    def language(self):
        return self._language  #aqui se creo un objeto del tipo property a languaje

    @language.setter  #aqui se puede instanciar ya que es un objeto de la clase language
    def language(self,value):
        self._language = value






try:
    Person(123)
except ValueError as ex:
    print(ex)