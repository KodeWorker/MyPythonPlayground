from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon

"""
This base window object for any applications developed on PyQt.
"""
class baseWindow(QMainWindow):
    
    def __init__(self, **kwargs):
        super().__init__()
        self.initParam(kwargs)
        self.initUI()
    
    def initParam(self, kwargs):
        default = {'width': None, 'height': None, 'loc': 'Center', 'title': 'base', 'dataPath': None, 'isFixed': True}
        
        arg_dict = default
        for key in default.keys():
            if key in kwargs.keys():
                arg_dict[key] = kwargs[key]
		
        self.width_ = arg_dict['width']
        self.height_ = arg_dict['height']
        self.loc = arg_dict['loc']
        self.title = arg_dict['title']
        self.dataPath = arg_dict['dataPath']
        self.isFixed = arg_dict['isFixed']
        
    def initUI(self):
        self.initWinSize()
        self.initWinLoc()
        self.initWinBasic()
        self.show()

    def initWinSize(self):
        if self.width_ == None:
            self.width_ = int (QDesktopWidget().screenGeometry(-1).width() / 2)
        if self.height_ == None:
            self.height_ = int (QDesktopWidget().screenGeometry(-1).height() / 2)
        self.resize(self.width_, self.height_)

    def initWinLoc(self):
        if self.loc == 'Center':
            qr = self.frameGeometry()
            cp = QDesktopWidget().screenGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        elif self.loc == 'TopLeft':
            qr = self.frameGeometry()
            cp = QDesktopWidget().screenGeometry().topLeft()
            qr.moveTopLeft(cp)
            self.move(qr.topLeft())
            
    def initWinBasic(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.dataPath + '/icon.png'))
        if self.isFixed:
            self.setFixedSize(self.width_, self.height_)