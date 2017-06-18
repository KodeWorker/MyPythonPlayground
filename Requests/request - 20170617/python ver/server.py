import socket
from DijkstrasAlgorithm import DijkstrasAlgorithm
from Graph import Graph, Node
    
def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    print('Server started')
    s.listen(5)
    c, addr = s.accept()
    
    while True:
        
        print('client connected ip: ' + str(addr) + '>')
        string = c.recv(1024).decode('utf-8')
        if not string:
            break
        if '[' in string:
            string = string.replace('[', '')
        if ']' in string:
            string = string.replace(']', '')
            
        L = string.split(',')
        source = int(L[0])
        target = int(L[1])
        
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
        
        path = DijkstrasAlgorithm(g, source, target)
        path_string = ','.join(str(e) for e in path)
        c.send(path_string.encode('utf-8'))
        
    s.close()

if __name__ == '__main__':
    Main()