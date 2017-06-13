# QLineEdit single line of text
# possible operations: undo redo cut paste drag&drop

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication

class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        
        qle.move(10, 100)        
        self.lbl.move(60, 40)
        
        # QLineEdit.textChanged
        qle.textChanged[str].connect(self.onChange)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()
        
    def onChange(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWidget()
    sys.exit(app.exec_())