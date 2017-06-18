class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.weights = {}
    
    def connect(self, node, weight):
        self.neighbors[node.name] = node
        self.weights[node.name] = weight
                    
        node.neighbors[self.name] = self
        node.weights[self.name] = weight

class Graph:
    def __init__(self):
        self.V = {}
        self.E = {}
    
    def addVertices(self, nodes):
        for n in nodes:
            self.V[n.name] = n
    
    def addEdges(self, edges):    
        # [ for each edge = [ init node name, end node name, weight], ...]
        for edge in edges:
            self.V[edge[0]].connect(self.V[edge[1]], edge[2])
        
if __name__ == '__main__':
    
    g = Graph()
    
    V = [Node(1), Node(2), Node(3), Node(4), Node(5), \
         Node(6), Node(7), Node(8), Node(9), Node(10)]
    E = [[1, 2, 1], \
         [1, 3, 3], \
         [1, 4, 3], \
         [2, 3, 1], \
         [2, 5, 1], \
         [2, 6, 8], \
         [3, 4, 1], \
         [3, 5, 1], \
         [3, 6, 1], \
         [3, 7, 2], \
         [4, 6, 2], \
         [4, 7, 3], \
         [4, 8, 1], \
         [5, 9, 1], \
         [6, 9, 1], \
         [6, 10, 7], \
         [7, 9, 3], \
         [7, 10, 2],\
         [8, 10, 4]]
    
    g.addVertices(V)
    g.addEdges(E)
