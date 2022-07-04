class Item(object):
    def __init__(self, unq_id, name, price, qty):
        self.unq_id = unq_id
        self.product_name = name
        self.price = price
        self.qty = qty


class Cart(object):
    def __init__(self):
        self.content = dict()

    def update(self, item):
        if item.unq_id not in self.content:
            self.content.update({item.unq_id: item})
            return
        for k, v in self.content.get(item.unq_id).items():
            if k == 'unq_id':
                continue
            elif k == 'qty':
                total_qty = v.qty + item.qty
                if total_qty:
                    v.qty = total_qty
                    continue
                self.remove_item(k)
            else:
                v[k] = item[k]

    def get_total(self):
        return sum([v.price * v.qty for _, v in self.content.items()])

    def get_num_items(self):
        return sum([v.qty for _, v in self.content.items()])

    def remove_item(self, key):
        self.content.pop(key)


if __name__ == '__main__':
    item1 = Item(1, "Banana", 1., 1)
    item2 = Item(2, "Eggs", 1., 2)
    item3 = Item(3, "Donut", 1., 5)
    cart = Cart()
    cart.update(item1)
    cart.update(item2)
    cart.update(item3)
    print ("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total()))
    cart.remove_item(1)
    print ("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total()))



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



