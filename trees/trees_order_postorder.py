#binary tree
#trees are hierarchical data structures
#full binary tree is a binary tree in which all nodes except leaf nodes have two children
#Depth First Traversals: 
#(a) Inorder (Left, Root, Right) : 4 2 5 1 3 
#(b) Preorder (Root, Left, Right) : 1 2 4 5 3 
#(c) Postorder (Left, Right, Root) : 4 5 2 3 1
# full binary tree is a special tree in which every parent has either two or no children
#perfect binary tree exactly two child nodes at the same level 
# balanced the difference of the left and the right is either 0 or 1 

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def inorder(root):
    if root:
        inorder(root.left) #traverse left
        print(str(root.val)) #imprimir valor de la raiz
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val))

def preorder(root):
    if root:
        print(str(root.val))
        preorder(root.left)
        preorder(root.right)

def traversePreOrder(self):
    print(self.val, end='') #esto basicamente imprime la raiz 
    if self.left:
        self.left.traversePreOrder()
    if self.right:
        self.right.traversePreOrder()

def traverseInOrder(self):
    if self.left:
        self.left.traverseInOrder()
    print(self.val , end='')
    if self.right:
        self.right.traverseInOrder()

def traversePostorder()
    if self.left:
        self.left.traversePostorder()
    if self.right:
        self.right.traversePostorder()
    print(self.val, end='')






root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

inorder(root)


#BST in python 


#the left subtree of node contains only nodes with keys lesser than the node's key
#the right subtree of a node contains only nodes with keys greater than the node's key
#the right and the leeft must also be a binary search tree
#there must be no duplicate nodes

#I need to know first the binary search 

#basic linear search approach

def find_linear(elements,value)
    for index, element in enumerate(elements):
        if element == value:
            return index 
#binary search
#divide the collection into 2 halves 
#elements in the collection must be sorted first
#lower boud and upper bound 
#divide and conquer algorithms quicksort, binary search
#if they request and algorith with low memory binary 
#if the memory is not a problem hash-based data structures

#mapping an element or one of its keys to the 
#element location in memory is referred to as hashing
#you compute the index based on the element itself
#data structure that uses this concep to map keys into values is called a map 
# a hash table dictionary or an associative array


#imagina que te dan un chingo de datos en cualquier formato no importa cual 
#entonces lo que tienes que hacer es hacer una listota y luego un diccionario

#mira el siguiente ejemplo

#duties for tomorrow hacer 3 programas que implementen este concepto
#remember to use helper functions
from benchmark import load_names 
names = load_names('names.txt')
index_by_name={
    name: index for index,name in enumerate(names)

}

'Guido van Rossum' in index_by_name

'Arnold Schwarzenegger' in index_by_name
True

index_by_name['Arnold Schwarzenegger']


#Implementing Binary Search in Python

def find_index(elements, value):
    left,right = 0, len(elements)-1
    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == value
            return middle

        if elements[middle] < value:
            left = middle +1
        elif elements[middle] > value:
            right = middle -1


#requiriments for the binary search tree 
#must be balanced 
#must be ordered 
def search(root,key):
    if root is None or root.val == key:
        return root
    #if is greater go to the right 
    if root.val < key:
        return search(root.right , key)

    #if no
    return search(root.left , key)

def search(root,key):
    if root is None or root.val == key:
        return root
    while root.val is not key:
        if root.val < key:
            root.right
        root.left
    return key 
    






































