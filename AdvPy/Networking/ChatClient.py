import socket
import threading
import time

tLock = threading.Lock()
iLock = threading.Lock()
shutDown = False

def receiving(name, sock):
    global shutDown
    
    while not shutDown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print('\n' + str(data.decode('utf-8')))
        except:
            pass
        finally:
            tLock.release()
            
def Main():    
    global shutDown
    
    host = '127.0.0.1'
    port = 0 # grab any free port
    
    server = ('127.0.0.1', 5000)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    
    s.setblocking(0)
    
    rT = threading.Thread(target=receiving, args=('RecvTread', s))
    rT.start()
    
    alias = input('Name: ')
    message = input(alias + '-> ')
    
    while message != 'q':
        if message != '':
            s.sendto((alias + ': ' + message).encode('utf-8'), server)
        iLock.acquire()
        time.sleep(0.2)
        message = input(alias + '-> ')
        iLock.release()
        
    
    shutDown = True
    rT.join()
    s.close()
    print('End connection')

if __name__ == '__main__':
    Main()