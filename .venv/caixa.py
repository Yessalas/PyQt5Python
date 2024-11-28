import sys
# importar os componentes para
# construção da janela
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
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

        #---------------- Criaro conteúdo da coluna da esquerda -------------------
        self.v_layout_esquerda = QVBoxLayout()

        #VAMOS CRIAR UMA LABEL PARA ADICIONAR O LOGODA NOSSA LOJA
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap(".venv/logo.png"))
        self.logo_label.setAlignment(Qt.AlignCenter)
        #ajuda a label e a imagem para ficar do tamanho ideal
        #self.logo_label.setScaledContents(True)
        # adicionar a label com a imagem na tela
        self.v_layout_esquerda.addWidget(self.logo_label)


        # vamos crias as labels e as LinesEdits que ficarão na coluna 
        # da esquerda, dentro do layout vertical da esquerda
        self.codigo_produto_label = QLabel("Código do Produto: ")
        self.codigo_produto_label.setStyleSheet("QLabel{font-size:12pt;color:#fff}")
        self.codigo_produto_edit = QLineEdit()
        self.codigo_produto_edit.setStyleSheet("QLineEdit{ padding: 5px;}")
        self.v_layout_esquerda.addWidget(self.codigo_produto_label)
        self.v_layout_esquerda.addWidget(self.codigo_produto_edit)

        self.nome_produto_label = QLabel("Nome do Produto: ")
        self.nome_produto_label.setStyleSheet("QLabel{font-size:12pt;color:#fff}")
        self.nome_produto_edit = QLineEdit()
        self.nome_produto_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.nome_produto_label)
        self.v_layout_esquerda.addWidget(self.nome_produto_edit)

        self.descricao_produto_label = QLabel("Código do Produto: ")
        self.descricao_produto_label.setStyleSheet("QLabel{font-size:12pt;color:#fff}")
        self.descricao_produto_edit = QLineEdit()
        self.descricao_produto_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.descricao_produto_label)
        self.v_layout_esquerda.addWidget(self.descricao_produto_edit)

        self.quantidade_produto_label = QLabel("Quantidade do Produto: ")
        self.quantidade_produto_label.setStyleSheet("QLabel{font-size:12pt;color:#fff}")
        self.quantidade_produto_edit = QLineEdit()
        self.quantidade_produto_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.quantidade_produto_label)
        self.v_layout_esquerda.addWidget(self.quantidade_produto_edit)

        self.preco_produto_label = QLabel("Preço Unitário do Produto: ")
        self.preco_produto_label.setStyleSheet("QLabel{font-size:12pt;color:#fff}")
        self.preco_produto_edit = QLineEdit()
        self.preco_produto_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.preco_produto_label)
        self.v_layout_esquerda.addWidget(self.preco_produto_edit)

        self.subtotal_produto_label = QLabel("Sub Total: ")
        self.subtotal_produto_label.setStyleSheet("QLabel{font-size:12pt;color:#fff}")
        self.subtotal_produto_edit = QLineEdit()
        self.subtotal_produto_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.subtotal_produto_label)
        self.v_layout_esquerda.addWidget(self.subtotal_produto_edit)

        # adicionar o layout vertical da esquerda com todos os controles:
        # label e lineEdit dentro da coluna da esquerda(label_coluna_esquerda)

        self.label_coluna_esquerda.setLayout(self.v_layout_esquerda)

        #------------------- controles da coluna da direita ------------------
        self.v_layout_direita = QVBoxLayout()
        # criar uma tabela e adicionar na coluna da direita 
        # esta tabela terá os nomes dos campos que estão ao esquerdo
        #colunas da tabela
        colunas = ["Cod.Produto", "Nome do Produto", "Descrição", "Quantidade", "Preço", "Sub-Total"]
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setRowCount(10)
        self.v_layout_direita.addWidget(self.tabela)

        self.total_pagar_label = QLabel("Total a pagar: ")
        self.total_pagar_label.setStyleSheet("QLabel{font-size:12pt;color:#fff}")
        self.total_pagar_edit = QLineEdit("0,00")
        self.total_pagar_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_direita.addWidget(self.total_pagar_label)
        self.v_layout_direita.addWidget(self.total_pagar_edit)

        self.label_coluna_direita.setLayout(self.v_layout_direita)










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
