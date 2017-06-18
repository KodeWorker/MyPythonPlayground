def DijkstrasAlgorithm(graph, source, target):
    Q = graph.V.copy()
    dist = {}
    prev = {}
    for name in graph.V:
        if name != source:
            dist[name] = float('inf')
        else:
            dist[name] = 0
        prev[name] = None
    
    while len(Q) != 0:
        # find vertice with min dist
        minLen = float('inf')
        minID = None
        for Q_id in Q:
            if dist[Q_id] < minLen:
                minLen = dist[Q_id]
                minID = Q_id
        
        # end condition
        if minID == target:
            break
        
        Q.pop(minID, None)
#        print(minID)
        for neighbor_id in graph.V[minID].neighbors:
            alt = dist[minID] + graph.V[minID].weights[neighbor_id]
            if alt < dist[neighbor_id]:
                dist[neighbor_id] = alt
                prev[neighbor_id] = minID
    
    # reverse the sequence and get the path
    path = []
    u = target
    while prev[u] != None:
        path.append(u)
        u = prev[u]
    path.append(u)
    
    return path[::-1]

        
if __name__ == '__main__':
    from Graph import Graph, Node
    
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
    
    path = DijkstrasAlgorithm(g, 1, 6)
