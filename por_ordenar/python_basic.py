class Item:
    def __init__(self, name , price):
        self.name = name
        self.price = price

        def getPrice(self):
            return self.price

        def getName(self):
            return self.name

class ShoppingCart():
        def __init__(self):
            self.items = []

        def add(self, item):
            self.items.append(item)

        def total(self):
            return sum(self.items)




class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

class Cart:
    def __init__(self, list):
        self.list = []

    def add(self, item):
        self.list.append(self.list)

    def getTotal(self):
        total = 0
        for item in self.list:
            name, price = item # or price = item[1]
            total = total + price

    def getNumItems(self):
        count = 0
        for c in range(self.list):
            count = self.list + 1
            return count

    def removeItem(self, item):
        pass
        #removes the item from the cart's item list
    # Implement the Item here
bike = Item("bike",1000)
headphones = Item('headphones',100)
cart = ShoppingCart()
print(cart.total())





print(bike.__dict__)
print(headphones.__dict__)


def __len__(self):
    return self.item_count