
def depth_first(graph,source):
    stack=[source]
    #how long we want to maintain the while cicle 
    while ( len(stack) > 0):
        current = stack.pop()
        print(current)
        
        for neighbor in  graph[current]:
            stack.append(neighbor)
            
graph = {
  'A' : ['B','C'],
  'B' : ['D'],
  'C' : ['E'],
  'D' : ['F'],
  'E' : [],
  'F' : []
}            

print(depth_first(graph,'A'))