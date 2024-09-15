"""
Construir un programa que muestre una ventana a traves de la
cual se pueda leer su numero de cedula y nombre completo
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow,QPushButton,QLineEdit,QLabel)
from PyQt5 import uic
import sys


class cedName(QMainWindow):
    def __init__(self):
        super().__init__()
    #Se llama al archivo del designer para ser utilizado.
        uic.loadUi(r"C:\progra3\LAB1_2\Laboratorio-1---Computo-2\disenioCedula.ui", self)
        self.nombre = self.findChild(QLineEdit,"lne1")
        self.cedula = self.findChild(QLineEdit,"lne2")
        self.boton = self.findChild(QPushButton,"btnMostrar")
        self.label = self.findChild(QLabel,"lbl3")
    #Se redirecciona a la funcion verCedula
        self.boton.clicked.connect(self.verCedula)

    def verCedula(self):
    #Se extraen los campos para posteriormente mostrarlos en el label 3
        nombre = self.nombre.text()
        cedula = self.cedula.text()
        self.label.setText(f"Nombre: {nombre}\nCédula: {cedula}") 
        self.nombre.clear()
        self.cedula.clear()


app = QApplication(sys.argv)
cedula= cedName()
cedula.show()
app.exec()