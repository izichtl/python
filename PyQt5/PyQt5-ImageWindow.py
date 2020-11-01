import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "JANELA 01"
        self.top   = 150
        self.left  = 300
        self.width = 600
        self.height = 400
        self.setWindowIcon(QtGui.QIcon('cat_.png'))
        self.InitWindow()

    def InitWindow(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)

            self.show()



App = QApplication(sys.argv)
janela = Window()
sys.exit(App.exec_())
