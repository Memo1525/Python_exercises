#
#  Having a single linked  list with the following data:
#
# employeeId : 001
# employeeName : Juan Perez
# employeeEMail : JuanPere@anygmail.com
# employeeNext : 002
#
# employeeId : 002
# employeeName : Antonio Ramos
# employeeEMail : YonyRamos@anygmail.com
# employeeNext : 003
#
# employeeId : 003
# employeeName : Pedro Paramo
# employeeEMail : PeterParamo@anygmail.com
# employeeNext : null
#
# Build a double linked  list e.g. where you can have reading and writing methods
#
# Upon migrated, new nodes in the double linked list will look like this :
#
# employeeId : 001
# employeeName : Juan Perez
# employeeEMail : JuanPere@anygmail.com
# employeeTop : latest node Id, if none point to the latest one so you create a circled list
# employeeNext : 002
#
# Finally, once double linked list has been populated, do the following:
# 1) Print out nodes info
# 2) delete employeeId : 002,
# 3) upon deleted, you should be able to list and print remaining nodes in the double linked list - reuse of #1
#
# Note. This is 30 mins code challenge assignment.
# me sali de la reunion??

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


'''
class single:
    def __init__(self):
        self.head = None
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval =printval.nref

lista=single()
lista.head = Node(['001','Juan Perez','JuanPere@anygmail.com','002'])
elemento2=Node(['002','Antonio Ramos','YonyRamos@anygmail.com','003'])
lista.head.nref = elemento2
elemento3=Node(['003','Pedro Paramo','PeterParamo@anygmail.com','null'])
lista.listprint()

'''


class double:
    def __init__(self):
        self.head = None

    def insertarVacio(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("lista vacia")

    def insertaralfinal(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def eliminar(self, posicion):
        if posicion == 1 and self.head != None:
            nodeborrar = self.head
            self.head = self.head.next
            nodeborrar = None
        if self.head != None:
            self.head.prev = None
        else:
            temp = self.head
        for i in range(1, posicion - 1):
            if (temp != None):
                temp = temp.next
            if (temp != None and temp.next != None):
                nodeborrar = temp.next
            if temp.next.next != None:
                temp.

    def mostrar(self):
        if self.head is None:
            print("lista vacia")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next


lista = double()
lista.insertarVacio(['001', 'Juan Perez', 'JuanPere@anygmail.com', '002'])
lista.insertaralfinal(['002', 'Antonio Ramos', 'YonyRamos@anygmail.com', '003'])
lista.mostrar()



Se