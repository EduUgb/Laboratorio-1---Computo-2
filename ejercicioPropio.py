"""
Después de realizar los cinco ejercicios realizar un ejercicio con la
librería de PyQt que utilice al menos dos de estos widgets:
radiobox, combobox y spinbox. El ejercicio debe permitir la entrada
de datos. Además, proporcionen una explicación detallada sobre
qué hace el programa y qué problema resuelve.
"""
#Compra de entradas de cine comunitario
"""
Se ha establecido un cine en la comunidad, el cual es comunitario y los precios no son tan elevados
pero al ser una comunidad pequeña desean que los vecinos puedan generar los tickets de compra para pagar
de forma presencial a la hora de ir al cine comunitario y agilizar las entradas, 
debido a que al ser tantos vecinos, se llena el establecimiento al momento de compras, y como
es comunitario solo trabajan 5 personas.

Cada pelicula tiene un precio distinto, al igual que los combos y horarios
"""


from PyQt5.QtWidgets import (QApplication, QMainWindow, QRadioButton, QLabel, QComboBox, QSpinBox, QLineEdit, QButtonGroup,QPushButton)
from PyQt5 import uic
import sys

class Cine(QMainWindow):
    def _init_(self):
        super()._init_()
        # Cargar el archivo .ui
        uic.loadUi(r"C:\Users\ar151\OneDrive\Escritorio\hola\Laboratorio-1---Computo-2\disenioTicket.ui", self)
        
        # Obtener referencias a los widgets
        self.nombre = self.findChild(QLineEdit, "lnenombre")
        self.combo = self.findChild(QComboBox, "combo")
        self.radio10 = self.findChild(QRadioButton, "radio10")
        self.radio5 = self.findChild(QRadioButton, "radio5")
        self.radio2 = self.findChild(QRadioButton, "radio2")
        self.radio7 = self.findChild(QRadioButton, "radio7")
        self.voletos = self.findChild(QSpinBox, "spinvoletos")
        self.comboPelicula = self.findChild(QComboBox, "combopelicula")
        self.label = self.findChild(QLabel, "lbl1")
        self.label2 = self.findChild(QLabel, "lbl2")
        self.generar = self.findChild(QPushButton, "btnTicket")
        self.generar.clicked.connect(self.salida)
        
        # Conectar las señales
        self.radio10.toggled.connect(self.Total)
        self.radio5.toggled.connect(self.Total)
        self.radio2.toggled.connect(self.Total)
        self.radio7.toggled.connect(self.Total)
        self.voletos.valueChanged.connect(self.Total)
        self.combo.currentIndexChanged.connect(self.Total)
        self.comboPelicula.currentIndexChanged.connect(self.Total)
        
        self.Total()

        self.radioGroup = QButtonGroup(self)
        self.radioGroup.addButton(self.radio10)
        self.radioGroup.addButton(self.radio5)
        self.radioGroup.addButton(self.radio2)
        self.radioGroup.addButton(self.radio7)

    def Total(self):
        total = 0
        
        # Calcular el total basado en los botones
        if self.radio10.isChecked():
            total += 2.25
        if self.radio5.isChecked():
            total += 3.00
        if self.radio2.isChecked():
            total += 3.00
        if self.radio7.isChecked():
            total += 4.00
        
        # Obtener el valor seleccionado en el combo de alimentos
        combo = 0
        if self.combo.currentIndex() == 0:
            combo = 0.00
        if self.combo.currentIndex() == 1:
            combo = 2.00
        elif self.combo.currentIndex() == 2:
            combo = 3.00
        elif self.combo.currentIndex() == 3:
            combo = 4.00
        
        total += combo
        
        # Obtener el valor seleccionado en el combo de las peliculas
        comboPeli = 0
        if self.comboPelicula.currentIndex() == 0:
            comboPeli = 0.00
        if self.comboPelicula.currentIndex() == 1:
            comboPeli = 7.00
        elif self.comboPelicula.currentIndex() == 2:
            comboPeli = 5.00
        elif self.comboPelicula.currentIndex() == 3:
            comboPeli = 12.00
        elif self.comboPelicula.currentIndex() == 4:
            comboPeli = 9.00
        elif self.comboPelicula.currentIndex() == 5:
            comboPeli = 4.00
        boletos = self.voletos.value()
        total += comboPeli * boletos

        # Mostrar el total
        self.label.setText(f"${total}")

    def salida(self):
        nombre = self.nombre.text()
        boleto = self.voletos.value()
        alimento = self.combo.currentText()
        rad10 = self.radio10.isChecked()
        rad5 = self.radio5.isChecked()
        rad2 = self.radio2.isChecked()
        rad7 = self.radio7.isChecked()
        peli = self.comboPelicula.currentText()
        total1 = self.label.text()

    #Modificamos el horario
        horario = ""
        if rad10:
            horario = "10:30 AM"
        elif rad5:
            horario = "5:00 PM"
        elif rad2:
            horario = "2:00 PM"
        elif rad7:
            horario = "7:00 PM"

        self.label2.setText(
            f"Nombre: {nombre}\n"
            f"Cantidad de boletos: {boleto}\n"
            f"Combo alimenticio: {alimento}\n"
            f"Pelicula: {peli}\n"
            f"Horario: {horario}\n"
            f"Total: {total1}"
        )
            # Limpiar campos
        self.nombre.clear()
        self.voletos.clear()
        self.combo.setCurrentIndex(0)
        self.comboPelicula.setCurrentIndex(0)


        self.radioGroup.setExclusive(False)
        self.radio10.setChecked(False)
        self.radio5.setChecked(False)
        self.radio2.setChecked(False)
        self.radio7.setChecked(False)




app = QApplication(sys.argv)
cinepolis = Cine()
cinepolis.show()
app.exec()