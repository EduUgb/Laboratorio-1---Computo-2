"""
Construir un programa que muestre una ventana en la cual 
aparezca su nombre completo
y su edad centrados.
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow,QPushButton,QLineEdit,QLabel)
from PyQt5 import uic
import sys


class datos(QMainWindow):
    def __init__(self):
        super().__init__()
    #Se llama al archivo del designer para ser utilizado junto a sus labels, line edits y botones
        uic.loadUi(r"C:\progra3\LAB1_2\Laboratorio-1---Computo-2\disenioEdad.ui", self)
    #Se busca el widget a utilizar mediante su nombre en el designer
        self.nombre = self.findChild(QLineEdit,"lne1")
        self.edad = self.findChild(QLineEdit,"lne2")
        self.boton = self.findChild(QPushButton,"btnMostrar")
        self.label = self.findChild(QLabel,"lbl3")
    #Se redirecciona a la funcion click
        self.boton.clicked.connect(self.click)

    def click(self):
    #Se extrae el nombre y la edad de los line edit y se asigna una salida al tercer label
        nombre = str(self.nombre.text())
    #La edad debe ser int
        edad = int(self.edad.text())
        self.label.setText(f"Nombre: {nombre}\nEdad: {edad} años") 
        self.nombre.clear()
        self.edad.clear()


app = QApplication(sys.argv)
datosShow = datos()
datosShow.show()
app.exec()