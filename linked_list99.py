class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes =[]
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " ->".join(nodes)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
#inserting a new node
    def add_first(self,node):
        node.next = self.head
        self.head = node
#inserting new node at the end
    def add_last(self,node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        

