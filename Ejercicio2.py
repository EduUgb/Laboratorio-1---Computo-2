"""
Construir un programa que muestre una ventana
y que lea una clave secreta sin mostrar los caracteres
que lo componen
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow,QWidget,QPushButton,QLineEdit,QFormLayout,QLabel)
from PyQt5 import uic
import sys


class password(QMainWindow):
    def __init__(self):
        super().__init__()
    #Se llama al archivo del designer para ser utilizado.
        uic.loadUi(r"C:\progra3\LAB1_2\Laboratorio-1---Computo-2\disenioPassword.ui", self)
        self.password = self.findChild(QLineEdit,"lne2")
        self.boton = self.findChild(QPushButton,"btnAcceder")
        self.label = self.findChild(QLabel,"lbl3")
    #Se redirecciona a la funcion mostrar
        self.boton.clicked.connect(self.mostrar)

    def mostrar(self):
    #Se extrae la contraseña del line edit y se pasa mediante un if para verificar que la contraseña sea correcta
        password = self.password.text()
        if password == "contraseña12":{
        self.label.setText("Tiene acceso al sistema")}
        else:{self.label.setText("Contraseña incorrecta")}
        self.password.clear()
     #Posdt: La contraseña no se muestra en el edit text, debido a la funcion Password del campo en el designer       


app = QApplication(sys.argv)
verificar = password()
verificar.show()
app.exec()