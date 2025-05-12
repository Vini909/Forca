import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

# Importação das interfaces
from pageInicial import Ui_MainWindow 
from pageCateg import Ui_MainWindow 
from pagePerdeu import Ui_MainWindow 
from pageVenceu import Ui_MainWindow 
from pont1 import Ui_MainWindow
from pont2 import Ui_MainWindow
from pont3 import Ui_MainWindow
from pont4 import Ui_MainWindow
from forca_game import Ui_MainWindow

class pageInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pageInicial.ui", self)
        
        self.pushButton.clicked.connect(self.ir_categ)
        self.pushButton_2.clicked.connect(self.ir_pont1)
    
    def ir_categ(self):
        self.pageCateg = pageCateg()
        self.pageCateg.show()
        self.close()
    
    def ir_pont1(self):
        self.pont1 = pont1()
        self.pont1.show()
        self.close()

class pont1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pont1.ui", self)
        self.voltar.clicked.connect(self.volt_inic)
        self.avancar_2.clicked.connect(self.ir_pont2)
    
    def volt_inic(self):
        self.pageInicial = pageInicial()
        self.pageInicial.show()
        self.close()
    
    def ir_pont2(self):
        self.pont2 = pont2()
        self.pont2.show()
        self.close()

class pont2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pont2.ui", self)
        self.pushButton_2.clicked.connect(self.volt_inic)
        self.pushButton.clicked.connect(self.ir_pont3)
    
    def volt_inic(self):
        self.pageInicial = pageInicial()
        self.pageInicial.show()
        self.close()
    
    def ir_pont3(self):
        self.pont3 = pont3()
        self.pont3.show()
        self.close()

class pont3(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pont3.ui", self)
        self.pushButton_2.clicked.connect(self.volt_inic)
    
    def volt_inic(self):
        self.pageInicial = pageInicial()
        self.pageInicial.show()
        self.close()

class pageCateg(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pageCateg.ui", self)
        self.pushButton_4.clicked.connect(self.volt_inic)
        self.pushButton_3.clicked.connect(self.ir_forc)
        self.pushButton_2.clicked.connect(self.ir_forc02)
        self.pushButton.clicked.connect(self.ir_forc03)
    
    def volt_inic(self):
        self.pageInicial = pageInicial()
        self.pageInicial.show()
        self.close()
    
#-----BOTÃO 01-----#
    def ir_forc(self):
        self.forca_game = forca_game()
        self.forca_game.show()
        self.close()

#-----BOTÃO 02-----#
    def ir_forc02(self):
        self.forca_game = forca_game02()
        self.forca_game.show()
        self.close()

#-----BOTÃO 03-----#
    def ir_forc03(self):
        self.forca_game = forca_game03()
        self.forca_game.show()
        self.close()

#----------LISTA 01----------#
class forca_game(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("forca_game.ui", self)
        self.pushButton_4.clicked.connect(self.volt_categ)
        self.pushButton.clicked.connect(self.animal)
        self.pushButton_2.clicked.connect(self.check_letter)  # Conecta o botão de tentativa
        self.carregar_pontuacao()
    
    def animal(self):
        self.animal = [
            "cachorro",
            "gato",
            "leão",
            "elefante",
            "tigre",
            "girafa",
            "zebra",
            "urso",
            "macaco",
            "lobo"
        ]       
        self.secreta = random.choice(self.animal)
        self.certa = ["_"] * len(self.secreta)
        self.errada = 1  # Inicializa o contador de erros
        
        self.create_labels()
    
    def create_labels(self):
        self.layout = QHBoxLayout()
        self.font = QFont("Arial", 50)  # Define a fonte e o tamanho
        self.labels = []
        for i in range(len(self.secreta)):
            label = QLabel("_")
            label.setFont(self.font)  # Aplica a fonte ao label
            label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label)
            self.labels.append(label)
        
        self.label_5.setLayout(self.layout)  # Adiciona o layout ao label_5
    
    def check_letter(self):
        letter = self.lineEdit.text().lower()  # Usa o QLineEdit existente
        if letter in self.secreta:
            for i, char in enumerate(self.secreta):
                if char == letter:
                    self.labels[i].setText(letter)
        
        else:
            self.errada += 1
            img = f"./Forca_img/0{self.errada}.png"
            piximg = QPixmap(img)
            self.label_3.setPixmap(piximg)
            
            self.perdeu()
     
        self.lineEdit.clear()


        if all(label.text() != "_" for label in self.labels):
            self.venceu()

        
    def carregar_pontuacao(self):
        try:
            with open("pontuacao.txt", "r") as f:
                self.pontuacao = int(f.read())
        except (FileNotFoundError, ValueError):
            self.pontuacao = 0

    def salvar_pontuacao(self):
        with open("pontuacao.txt", "w") as f:
            f.write(str(self.pontuacao))
    
    def perdeu(self):
        if self.errada == 7:
            self.pagePerdeu = pagePerdeu()
            self.pagePerdeu.show()
            self.close()
    
    def venceu(self):
            self.pontuacao += 100
            self.salvar_pontuacao()
            self.pageVenceu = pageVenceu()
            self.pageVenceu.show()
            self.close()

        
    def volt_categ(self):
        self.pageCateg = pageCateg()
        self.pageCateg.show()
        self.close()

#----------LISTA 02----------#

class forca_game02(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("forca_game.ui", self)
        self.pushButton_4.clicked.connect(self.volt_categ)
        self.pushButton.clicked.connect(self.comidas)
        self.pushButton_2.clicked.connect(self.check_letter)  # Conecta o botão de tentativa
        self.carregar_pontuacao()
    
    def comidas(self):
        self.comidas = [
            "pizza",
            "hambúrguer",
            "arroz",
            "feijão",
            "lasanha",
            "sushi",
            "salada",
            "frango assado",
            "macarrão",
            "panqueca"
        ]     
        self.secreta = random.choice(self.comidas)
        self.certa = ["_"] * len(self.secreta)
        self.errada = 1  # Inicializa o contador de erros
        
        self.create_labels()
    
    def create_labels(self):
        self.layout = QHBoxLayout()
        self.font = QFont("Arial", 50)  # Define a fonte e o tamanho
        self.labels = []
        for i in range(len(self.secreta)):
            label = QLabel("_")
            label.setFont(self.font)  # Aplica a fonte ao label
            label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label)
            self.labels.append(label)
        
        self.label_5.setLayout(self.layout)  # Adiciona o layout ao label_5
    
    def check_letter(self):
        letter = self.lineEdit.text().lower()  # Usa o QLineEdit existente
        if letter in self.secreta:
            for i, char in enumerate(self.secreta):
                if char == letter:
                    self.labels[i].setText(letter)
        
        else:
            self.errada += 1
            img = f"./Forca_img/0{self.errada}.png"
            piximg = QPixmap(img)
            self.label_3.setPixmap(piximg)
            
            self.perdeu()
     
        self.lineEdit.clear()


        if all(label.text() != "_" for label in self.labels):
            self.venceu()
   
    def carregar_pontuacao(self):
        try:
            with open("pontuacao.txt", "r") as f:
                self.pontuacao = int(f.read())
        except (FileNotFoundError, ValueError):
            self.pontuacao = 0

    def salvar_pontuacao(self):
        with open("pontuacao.txt", "w") as f:
            f.write(str(self.pontuacao))

    def perdeu(self):
        if self.errada == 7:
            self.pagePerdeu = pagePerdeu()
            self.pagePerdeu.show()
            self.close()
    
    def venceu(self):
            self.pontuacao += 100
            self.salvar_pontuacao()
            self.pageVenceu = pageVenceu()
            self.pageVenceu.show()
            self.close()

    def volt_categ(self):
        self.pageCateg = pageCateg()
        self.pageCateg.show()
        self.close()

#----------LISTA 03----------#

class forca_game03(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("forca_game.ui", self)
        self.pushButton_4.clicked.connect(self.volt_categ)
        self.pushButton.clicked.connect(self.objetos)
        self.pushButton_2.clicked.connect(self.check_letter)  # Conecta o botão de tentativa
        self.carregar_pontuacao()
    
    def objetos(self):
        self.objetos = [
            "cadeira",
            "mesa",
            "lápis",
            "caderno",
            "computador",
            "celular",
            "garrafa",
            "mochila",
            "óculos",
            "controle remoto"
        ]   
        self.secreta = random.choice(self.objetos)
        self.certa = ["_"] * len(self.secreta)
        self.errada = 1  # Inicializa o contador de erros
        
        self.create_labels()
    
    def create_labels(self):
        self.layout = QHBoxLayout()
        self.font = QFont("Arial", 50)  # Define a fonte e o tamanho
        self.labels = []
        for i in range(len(self.secreta)):
            label = QLabel("_")
            label.setFont(self.font)  # Aplica a fonte ao label
            label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label)
            self.labels.append(label)
        
        self.label_5.setLayout(self.layout)  # Adiciona o layout ao label_5
    
    def check_letter(self):
        letter = self.lineEdit.text().lower()  # Usa o QLineEdit existente
        if letter in self.secreta:
            for i, char in enumerate(self.secreta):
                if char == letter:
                    self.labels[i].setText(letter)
        
        else:
            self.errada += 1
            img = f"./Forca_img/0{self.errada}.png"
            piximg = QPixmap(img)
            self.label_3.setPixmap(piximg)
            
            self.perdeu()
     
        self.lineEdit.clear()


        if all(label.text() != "_" for label in self.labels):
            self.venceu()

        
    def carregar_pontuacao(self):
        try:
            with open("pontuacao.txt", "r") as f:
                self.pontuacao = int(f.read())
        except (FileNotFoundError, ValueError):
            self.pontuacao = 0

    def salvar_pontuacao(self):
        with open("pontuacao.txt", "w") as f:
            f.write(str(self.pontuacao))




    
    def perdeu(self):
        if self.errada == 7:
            self.pagePerdeu = pagePerdeu()
            self.pagePerdeu.show()
            self.close()
    
    def venceu(self):
            self.pontuacao += 100
            self.salvar_pontuacao()
            self.pageVenceu = pageVenceu()
            self.pageVenceu.show()
            self.close()

        
    def volt_categ(self):
        self.pageCateg = pageCateg()
        self.pageCateg.show()
        self.close()

class pagePerdeu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pagePerdeu.ui", self)




class pont4(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pont4.ui", self)

        self.carregar_pontuacao()
        self.imag()
        self.create_labels()
    
    def create_labels(self):
        self.layout = QHBoxLayout()
        self.font = QFont("Arial", 50)  # Define a fonte e o tamanho
        self.score_label = QLabel(f"Pontuação: {self.pontuacao}")
        self.score_label.setFont(QFont("Arial", 20))
        self.score_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.score_label)

        
        self.label_5.setLayout(self.layout)  # Adiciona o layout ao label_5
        
     
    def carregar_pontuacao(self):
        try:
            with open("pontuacao.txt", "r") as f:
                self.pontuacao = int(f.read())
        except (FileNotFoundError, ValueError):
            self.pontuacao = 0


    def imag(self):
        if self.pontuacao >= 500 and self.pontuacao <= 999:
            img = f"./Forca_img/11.png"
            piximg = QPixmap(img)
            self.label_4.setPixmap(piximg)
        else:
            if self.pontuacao >= 1000 and self.pontuacao <= 1499:
                img = f"./Forca_img/20.png"
                piximg = QPixmap(img)
                self.label_4.setPixmap(piximg) 
            else:
                if self.pontuacao >= 1500 and self.pontuacao <= 1999:
                    img = f"./Forca_img/30.png"
                    piximg = QPixmap(img)
                    self.label_4.setPixmap(piximg) 
                else:
                    if self.pontuacao >= 2000 and self.pontuacao <= 2499:
                        img = f"./Forca_img/12.png"
                        piximg = QPixmap(img)
                        self.label_4.setPixmap(piximg) 
                    else:
                        if self.pontuacao >= 2500 and self.pontuacao <= 2999:
                            img = f"./Forca_img/21.png"
                            piximg = QPixmap(img)
                            self.label_4.setPixmap(piximg) 
                        else:
                            if self.pontuacao >= 3000 and self.pontuacao <= 4999:
                                img = f"./Forca_img/31.png"
                                piximg = QPixmap(img)
                                self.label_4.setPixmap(piximg) 
                            else:
                                if self.pontuacao >= 5000:
                                    img = f"./Forca_img/40.png"
                                    piximg = QPixmap(img)
                                    self.label_4.setPixmap(piximg) 
                
    

class pageVenceu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pageVenceu.ui", self)

        self.pushButton.clicked.connect(self.ir_score)

    def ir_score(self):
        self.pont4 = pont4()
        self.pont4.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = pageInicial()
    window.show()
    sys.exit(app.exec_())
