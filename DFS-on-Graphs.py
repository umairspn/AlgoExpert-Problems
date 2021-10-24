  
from collections import defaultdict
  
class Graph:
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
  
    def addEdge(self, start, end):
        self.graph[start].append(end)
  
    def showGraph(self):
        print(self.graph)
    
    def printAllPathsUtil(self, start, end, visited, path):
 
        visited[start]= True
        path.append(start)
 
        if start == end:
            print(path)
        else:
            for neighbor in self.graph[start]:
                if visited[neighbor]== False:
                    self.printAllPathsUtil(neighbor, end, visited, path)
                
        path.pop()
        visited[start]= False
  
    def printAllPaths(self, start, end):
        # self.V = no. of vertices = 4 --> 0,1,2,3
        visited =[False]*(self.V)
        print(visited)
        # visited = [F,F,F,F]
        path = []
        self.printAllPathsUtil(start, end, visited, path)
  

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)
  
g.showGraph()

s = 0 ; d = 1
print ("Following are all different paths from % d to % d :" %(s, d))
g.printAllPaths(s, d)