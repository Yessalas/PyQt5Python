import sys
# importar os componentes para
# construção da janela
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout
#construção da classe janela com o nome de caixa
class caixa(QWidget):
    #criação do método __init__ que inicia a janela
    # e exibe ela em tela
    def __init__(self):
        super().__init__()
        #vamos definir a posição e o tamnho da tela
        self.setGeometry(0,30,1000,800)

        #vamos definir o titúlo da nossa tela
        self.setWindowTitle("Caixa da loja")
        #vamos criar as labels que representam as colunas esquerda e direita

        #label da esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#769ce3}")

        #label da direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#a8bfe9}")


        #criar o layout horizontal para as colunas
        self.h_layout = QHBoxLayout()

        #Vamos adicionar as colunas, esquerda e direita ao layout horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        #adicionar o layout na tela
        self.setLayout(self.h_layout)



app = QApplication(sys.argv)
cx = caixa()
cx.show()
app.exec_()
