"""
Construir un programa que muestre una ventana en la cual 
aparezca su nombre completo
y su edad centrados.
"""
#Carlos Eduardo García Castillo SMSS045523

from PyQt5.QtWidgets import (QApplication, QMainWindow,QWidget,QPushButton,QLineEdit,QFormLayout,QLabel)
from PyQt5 import uic
import sys


class datos(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\progra3\LAB1_2\Laboratorio-1---Computo-2\disenioEdad.ui", self)
        self.nombre = self.findChild(QLineEdit,"lne1")
        self.edad = self.findChild(QLineEdit,"lne2")
        self.boton = self.findChild(QPushButton,"btnMostrar")
        self.label = self.findChild(QLabel,"lbl3")
        self.boton.clicked.connect(self.click)

    def click(self):
        nombre = self.nombre.text()
        edad = int(self.edad.text())
        self.label.setText(f"Nombre: {nombre}\nEdad: {edad} años") 
        self.nombre.clear()
        self.edad.clear()


app = QApplication(sys.argv)
datosShow = datos()
datosShow.show()
app.exec()