import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    # sys.argv is the args from commandline
    # every PyQt5 must create app. object
    app = QApplication(sys.argv)
    
    # Setting window propertires in memory
    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('Hello World!')
    # display the window
    w.show()
    
    # MAINLOOP
    
    # makes sure the clean exit
    sys.exit(app.exec_())