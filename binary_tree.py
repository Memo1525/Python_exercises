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

#           1
#          / \
#         2   3
#       /       \
#    4             5
#
#
#
#
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

inorder(root)