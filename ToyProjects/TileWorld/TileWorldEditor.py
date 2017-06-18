import os
import sys
from PyQt5.QtWidgets import QApplication

from Lib.base import baseWindow
from PyQt5.QtWidgets import QAction, QToolBar, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon

class newTileWorldWidget(QWidget):
    
    def __init__(self, parent=None):
        super(newTileWorldWidget ,self).__init__()
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.setEnabled(False)
        self.setWindowTitle('New World')
        self.setFixedSize(300, 300)        
        self.show()
    
    def closeEvent(self, event):
        self.parent.setEnabled(True)

class tileWorldEditorWindow(baseWindow):
    
    def initUI(self):
        self.initWinSize()
        self.initWinLoc()
        self.initWinBasic()
        
        self.initMenuBar()
        self.show()

    def initMenuBar(self):
        # all action settings of File tab in menu
        fileDict = {
        'newAction' : {'image': 'new.png', 'name': 'New', 'shortcut': 'Ctrl+N', 'action': self.new},
        'exitAction' : {'image': 'exit.png', 'name': 'Exit', 'shortcut': 'Ctrl+Q', 'action': QApplication.instance().quit}
        }
        
        # bind actions to filAction dict
        fileAction = {}
        for key in fileDict.keys():
            fileAction[key] = QAction(QIcon(self.dataPath + '/' + fileDict[key]['image']), fileDict[key]['name'], self)
            fileAction[key].setShortcut(fileDict[key]['shortcut'])
            fileAction[key].triggered.connect(fileDict[key]['action'])
        
        menubar = self.menuBar()
        # add all actions to File tab
        fileMenu = menubar.addMenu('&File')
        for key in fileAction.keys():
            fileMenu.addAction(fileAction[key])        

    def new(self):
        print('[Action]: new file opened!')
        newWorld = newTileWorldWidget(self)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(newWorld)
        
def Main():
    app = QApplication(sys.argv)
    w = tileWorldEditorWindow(
    width=1024,
    height=768,
    title='TileWorldEditor',
    dataPath=os.path.join(os.path.dirname(__file__), 'Data', 'Image', 'TileWorldEditor'))
    sys.exit(app.exec_())

if __name__ == '__main__':
    Main()