import socket

def Main():
    
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket()
    s.connect((host,port))
    
    filename = input('filename? -> ')
    if filename != 'q':
        s.send(filename.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        if data[:6] == 'EXISTS':
            filesize = float(data[6:])
            message = input('File Exists. ' + str(filesize) + ' bytes. Download? (y/n) ->' )
            if message == 'y' or message == 'Y':
                s.send('ok'.encode('utf-8'))
                f = open('new_' + filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print('\r{0:.2f}'.format((totalRecv/float(filesize))*100)+ '% Done', end='\r')
                print('\nDownlaod complete!')
        else:
            print('File dose not exist!')
    s.close()
    
if __name__ == '__main__':
    Main()