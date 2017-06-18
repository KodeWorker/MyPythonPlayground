# QPixmap is opt. to work with images on screen

import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap

class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('NightSky.jpg')
        
        # put the pixmap into the QLabel widget
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('Night Sky')
        self.show()  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWidget()
    sys.exit(app.exec_())