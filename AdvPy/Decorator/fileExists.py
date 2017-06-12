import os

def Exists(oldFunc):    
    def inside(filename):
        if os.path.exists(filename):
            oldFunc(filename)
        else:
            print('The file dose not exist.')
        
    return inside

@Exists
def outputLine(inFile):
    with open(inFile) as f:
        print(f.readlines())
    
def Main():            
#    func = Exists(outputLine)
#    func('fileExists.py')
#    func('test.py')
    
    outputLine('fileExists.py')
    outputLine('test.py')
    
if __name__ == '__main__':
    Main()
    