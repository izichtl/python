import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class Ventana(QMainWindow):
    def __init__(seft):

        QMainWindow.__init__(self)
        uic.loadUi("mainwindow.ui", self)


app = QApplication(sys.argv)
_a = Ventana()
_a.show()

app.exec_()
