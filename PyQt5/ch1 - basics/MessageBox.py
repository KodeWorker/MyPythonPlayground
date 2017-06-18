import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class myWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltip')
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self,          # question icon is shown
            'Message',                              # title
            "Are you sure to quit?",                # message
            QMessageBox.Yes | QMessageBox.No,       # standard buttons
            QMessageBox.No)                         # default button

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWidget()
    sys.exit(app.exec_())