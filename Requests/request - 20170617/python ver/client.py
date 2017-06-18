import socket

def Main():
    
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket()
    s.connect((host,port))
    
    source = input('[source,target] number? -> (q:exit)')
    while source != 'q':
        s.send(source.encode('utf-8'))    
        data = s.recv(1024).decode('utf-8')        
        print('min-cost path : %s' %(data))
        source = input('(source,target) number? -> (q:exit)')
    s.close()
    
if __name__ == '__main__':
    Main()