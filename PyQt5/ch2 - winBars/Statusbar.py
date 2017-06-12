import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.resize(250, 150)
        self.statusBar().showMessage('Status: Ready')
        self.setWindowTitle('Statusbar')    
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  