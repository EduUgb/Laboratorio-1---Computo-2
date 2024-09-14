"""
Construir un programa que muestre una ventana
y que lea una clave secreta sin mostrar los caracteres
que lo componen
"""
#Carlos Eduardo García Castillo SMSS045523

from PyQt5.QtWidgets import (QApplication, QMainWindow,QWidget,QPushButton,QLineEdit,QFormLayout,QLabel)
from PyQt5 import uic
import sys


class password(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\progra3\LAB1_2\Laboratorio-1---Computo-2\disenioPassword.ui", self)
        self.password = self.findChild(QLineEdit,"lne2")
        self.boton = self.findChild(QPushButton,"btnMostrar")
        self.label = self.findChild(QLabel,"lbl3")
        self.boton.clicked.connect(self.mostrar)

    def mostrar(self):
        password = self.password.text()
        if password == "contraseña12":{
        self.label.setText("Tiene acceso al sistema")}
        else:{self.label.setText("Contraseña incorrecta")}
        self.password.clear()
        


app = QApplication(sys.argv)
verificar = password()
verificar.show()
app.exec()