#understand what it is 
# bfs is a algorithms used to traverse a graph or a tree 
#the porpose of the algotithm is to visit all node vertex while avoiging cicles 

class Node:
    def __init__(self,data) :
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                    
root = Node('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')                     

#-----------------------------------------------------------
#another way to do 
""" graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A') """


#graph = node + edges 
#directed graph has arrows 
#undirected graphs don't have arrows 


#graph can be represented with adjacency list 
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

#depth first traversal  # stack  LIFO
#the direction that you choose you must go ahead with this until you satisfy 
#one direction as far as posible until you turn 

#breath first traversal  #queue FIFO
# tend to explore all directions all neighoborgouds 
sumatoria=0
for i in range(11):
  sumatoria+=i
  
print(sumatoria )
# es posible pasßarle un iterable a la funcion sum e imprimira la suma de lo que le pasemos 
