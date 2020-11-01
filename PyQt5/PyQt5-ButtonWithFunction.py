import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLineEdit, QLabel
from PyQt5 import QtCore
class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 400
        self.altura = 250
        self.title = "Primeira Janela"
        self.setStyleSheet('QtMainWindow {background-color:blue}')


        botao1 = QPushButton('botao1', self)
        botao1.move(50, 150)
        botao1.resize(200, 30)
        #botao.setStyleSheet()
        botao1.clicked.connect(self.botao_click)



        self.titulo = QLabel(self)
        self.titulo.setText('a clicar')
        self.titulo.move(100, 100)
        self.titulo.resize(300, 25)
        self.titulo.setStyleSheet('QLabel {color: #ababab; font-size: 30px}')



        self.texto_input = QLineEdit( self)
        self.texto_input.move(150,50)

        self.texto_input.connect(self.textInput1)

        '''
        texto_input1 = QLineEdit('Gramas da Porção', self)
        texto_input1.move(150,95)
        '''


        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.title)
        self.show()

    def botao_click(self):
        #self.titulo.setText('Clicado')
        self.texto_input.connect(self.textInput1)

    def textInput1(self, Calorias):
        cc = self
        cc * 2
        self.titulo.setText('Clicado %i' %(cc))











app = QApplication(sys.argv)

j= Janela()

sys.exit(app.exec_())
