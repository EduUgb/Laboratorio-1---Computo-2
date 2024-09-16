"""
Construir un programa el cual pueda leer 10 datos caracteristicos de una persona
"""


from PyQt5.QtWidgets import (QApplication, QMainWindow,QPushButton,QLineEdit,QLabel,QSpinBox,QComboBox)
from PyQt5 import uic
import sys

class caracter(QMainWindow):
    def _init_(self):
        super()._init_()
    #Se llama al archivo del designer para ser utilizado.

        uic.loadUi(r"C:\Users\ar151\OneDrive\Escritorio\hola\Laboratorio-1---Computo-2\disenioCaracteristicas.ui", self)
        self.nombre = self.findChild(QLineEdit,"lnenombre")
        self.ojos = self.findChild(QLineEdit,"lneojos")
        self.piel = self.findChild(QLineEdit,"lnepiel")
        self.altura = self.findChild(QLineEdit,"lnealtura")
        self.pelo = self.findChild(QLineEdit,"lnepelo")
        self.sangre = self.findChild(QLineEdit,"lnesangre")
        self.genero = self.findChild(QLineEdit,"lnegenero")
        self.nacimiento = self.findChild(QLineEdit,"lnenacimiento")
        self.edad = self.findChild(QSpinBox,"spinedad")
        self.civil = self.findChild(QComboBox,"combocivil")
        self.mostrar = self.findChild(QPushButton,"btnMostrar")
        self.label = self.findChild(QLabel,"lbl1")
    #Se redirecciona a la funcion 
        self.mostrar.clicked.connect(self.caracteristicas)

    def caracteristicas(self):
    #Se extraen los campos para posteriormente mostrarlos en el label 
        nombre = self.nombre.text()
        ojos = self.ojos.text()
        piel = self.piel.text()
        altura = self.altura.text()
        pelo = self.pelo.text()
        sangre = self.sangre.text()
        genero = self.genero.text()
        nacimiento = self.nacimiento.text()
        edad = self.edad.value()
        civil = self.civil.currentText()
        
        # Mostrar los datos en el QLabel
        self.label.setText(
            f"Nombre: {nombre}, "
            f"Ojos: {ojos}, "
            f"Piel: {piel}, "
            f"Altura: {altura}\n"
            f"Pelo: {pelo}, "
            f"Sangre: {sangre}, "
            f"Género: {genero}, "
            f"Nacimiento: {nacimiento}\n"
            f"Edad: {edad}, "
            f"Estado Civil: {civil}"
        )
        
        # Limpiar campos
        self.nombre.clear()
        self.ojos.clear()
        self.piel.clear()
        self.altura.clear()
        self.pelo.clear()
        self.sangre.clear()
        self.genero.clear()
        self.nacimiento.clear()
        self.edad.setValue(0)
        self.civil.setCurrentIndex(0)



app = QApplication(sys.argv)
caracteristica= caracter()
caracteristica.show()
app.exec()