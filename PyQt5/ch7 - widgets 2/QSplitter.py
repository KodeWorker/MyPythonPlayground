# QSplitter lets the user control the size of child widgets

import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory, QApplication
# QStyleFactory ???
from PyQt5.QtCore import Qt

class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        hbox = QHBoxLayout(self)
        
        # We use a styled frame in order to see the boundaries between the QFrame widgets.
        
        # child widget #1
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        # child widget #2
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        # child widget #3
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWidget()
    sys.exit(app.exec_())