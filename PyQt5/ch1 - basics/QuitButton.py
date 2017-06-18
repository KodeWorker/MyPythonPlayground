import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        
        btn = QPushButton('Quit', self)
        
        # connect the event signal to slot -> quit() function in QCoreApplication
        btn.clicked.connect(QCoreApplication.instance().quit)
#        btn.clicked.connect(print_string)
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltip')
        self.show()

def print_string():
    print('QUIT')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWidget()
    sys.exit(app.exec_())