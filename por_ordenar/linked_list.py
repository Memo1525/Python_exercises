class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def printLL(self):
        nodes = self.head
        while nodes is not None:
            print(nodes.data)
            nodes = nodes.next




    def add_front(self,new_data):
        dato =Node(new_data)  #creamos el nuevo nodo y lo asignamos a una variable en este caso dato
        dato.next = self.head #ponemos como siguiente el primer nodo de la lista ligada
        self.head = dato #ponemos como head el nodo que acabamos de agregar
    def add_front2(self,new_data):
        dato = Node(new_data) #creamos el nuevo nodo y lo asignamos a una variable en este caso dato
        dato.next = self.head # ponemos como siguiente el primer nodo de la lista ligada
        self.head = dato # y hacemos head el nodo que acabamos de agregar


    def append_final(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node


    def middle(self,prev_node,new_data):
        # checar que exista
        if prev_node is None:
            print("The node must be in the LL")
        new_node = Node(new_data) #creamos el nuevo nodo una vez que checamos de su existencia
        new_node.next = prev_node.next  #ponemos el next del nuevo nodo como el next del anterior
        prev_node.next = new_node #ponemos como next el anterior nodo

    #no se necesita iterar nada ya que se encuentran ya los nodos y se tiene ese supuesto y se camina bajo ese supuesto
    #Given a ‘key’, delete the first occurrence of this key in the linked list.

        # Given a reference to the head of a list and a key,
        # delete the first occurrence of key in linked list
    def deleteNode(self, key):            #para borrar un nodo que debemos de checar
                                              #checar que no este vacia la lista lo cual es siempre
                                              #irnos por el caso mas sencillo que en este caso es que el nodo a borrar este al inicio
            # Store head node
            temp = self.head

            if (temp is not None): # checamos que la lista no este vacia
                if (temp.data == key):
                    self.head = temp.next #se hace la asignacion
                    temp = None # se borra toda la informacion
                    return 'nodo eliminado correctamente '

            if temp is not None: #checa que no este vacio
                if temp.data == key:
                    self.head = temp.next #esto hace la asignacion
                    temp = None #borra todos los datos
                    return

            while (temp is not None):  #empezamos desde el head y nos ponemos a buscar como todas unas locas por toda la lista ligada
                    if temp.data == key:
                        break
                    prev = temp # se guarda el valor del nodo anterior el cual estaremos restableciendo cada vuelta
                    temp = temp.next

                    # if key was not present in linked list
            if (temp == None):
                    return ValueError('key is not a node ')

                    # Unlink the node from linked list
            prev.next = temp.next #asignamos el siguiente del nodo borrado al nodo anterios

            temp = None

    def deleteNode2(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next #aqui se hace la eliminacion
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None: #checamos que la lista no este vacia
            if index == position:
                temp = current.next #se liga el next del anterior del borrado al nuevo nodo
                break
            prev = current #se asigna el valor del nodo anterior al que se checa
            current = current.next #se mueve current al siguiente nodo
            index += 1
        prev.next = temp #se asignan los valores al previo y desaparece temp y el nodo borrado
        return prev










#tasks
# 1 insert the node at the end
# 2 insert the node at the beggining
# 3 insert the node at a given index

#como lo harias tu

objeto = Linkedlist()

objeto.head=Node(1)
el2=Node(2)
el3=Node(3)
objeto.head.next = el2
el2.next = el3
objeto.add_front(34)
objeto.append_final(23)
objeto.deleteNode(3)
objeto.deleteNode2(0)



#objeto.deleteNode()
objeto.printLL()






