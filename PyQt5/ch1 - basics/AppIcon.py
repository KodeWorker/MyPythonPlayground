import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # Setting locaion and size
        self.setGeometry(300, 300, 300, 220)
        
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('python.png'))
        
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w = myWidget()
    sys.exit(app.exec_())