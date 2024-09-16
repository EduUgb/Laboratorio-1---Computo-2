"""Construir un programa que muestre una ventana a traves de la cual se
puedan leer 3 datos basicos de 3 mascotas diferentes"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, QLabel)
from PyQt5 import uic
import sys

#Crearemos una lista la cual nos permita almacenar los datos de las 3 mascotas
listMascota = []

#Creamos una clase sobre las mascotas que incluya 4 elementos o atributos:
class Mascot:
    def __init__(self, nomb, age, especie, raza):
        self.nomb = nomb
        self.age = age
        self.especie = especie
        self.raza = raza

# Clase principal para la interfaz gráfica
class mascotReg(QMainWindow):
    def __init__(self):
        super().__init__()
       #Llamamos la ruta del archivo del designer que utilizaremos
       #Debe colocar la ruta de su dispositivo con \el nombre del archivo designer al final
        uic.loadUi(r"C:\Users\ar151\OneDrive\Escritorio\hola\Laboratorio-1---Computo-2\disenioMascota.ui", self)

        self.nombreAn = self.findChild(QLineEdit, "nomAn")
        self.edadAn = self.findChild(QLineEdit, "ageAn")
        self.especieAn = self.findChild(QLineEdit, "especieAn")
        self.razaAn = self.findChild(QLineEdit, "razaAn")
        self.boton = self.findChild(QPushButton, "btnGuardar")
        self.lblnom1 = self.findChild(QLabel, "lblNom1")
        self.lblnom2 = self.findChild(QLabel, "lblNom2")
        self.lblnom3 = self.findChild(QLabel, "lblNom3")
        self.lblAge1 = self.findChild(QLabel, "lblAge1")
        self.lblAge2 = self.findChild(QLabel, "lblAge2")
        self.lblAge3 = self.findChild(QLabel, "lblAge3")
        self.lblespe1 = self.findChild(QLabel, "lblEspe1")
        self.lblespe2 = self.findChild(QLabel, "lblEspe2")
        self.lblespe3 = self.findChild(QLabel, "lblEspe3")
        self.lblraza1 = self.findChild(QLabel, "lblRaza1")
        self.lblraza2 = self.findChild(QLabel, "lblRaza2")
        self.lblraza3 = self.findChild(QLabel, "lblRaza3")

        #Redireccionamos a funcion de guardado y actualizar(Aunque esta redirección se encontrará dentro de la función de guardar)
        self.boton.clicked.connect(self.ClickBtnGuardar)

    # Función para guardar los datos de las mascotas
    def ClickBtnGuardar(self):
        global listMascota  # Referenciamos la lista global
        nom = self.nombreAn.text()
        edad = self.edadAn.text()
        especie = self.especieAn.text()
        raza = self.razaAn.text()

        # Creamos una nueva instancia de Mascot y la añadimos a la lista
        newPet = Mascot(nom, edad, especie, raza)
        listMascota.append(newPet) 

        # Actualizamos las etiquetas después de añadir la mascota
        self.ActualizarLabels()

    # Función para actualizar los labels
    def ActualizarLabels(self):
       #Actualizamos los datos de las 3 mascotas segun la cantidad de datos que tenga la lista, esto lo hacemos mediante el if
       #Y en los else vaciamos los datos para que no afecte en la ejecución del programa
        if len(listMascota) > 0:
            self.lblnom1.setText(listMascota[0].nomb)
            self.lblAge1.setText(listMascota[0].age)
            self.lblespe1.setText(listMascota[0].especie)
            self.lblraza1.setText(listMascota[0].raza)
        else:
            self.lblnom1.setText("")
            self.lblAge1.setText("")
            self.lblespe1.setText("")
            self.lblraza1.setText("")

        if len(listMascota) > 1:
            self.lblnom2.setText(listMascota[1].nomb)
            self.lblAge2.setText(listMascota[1].age)
            self.lblespe2.setText(listMascota[1].especie)
            self.lblraza2.setText(listMascota[1].raza)
        else:
            self.lblnom2.setText("")
            self.lblAge2.setText("")
            self.lblespe2.setText("")
            self.lblraza2.setText("")

        if len(listMascota) > 2:
            self.lblnom3.setText(listMascota[2].nomb)
            self.lblAge3.setText(listMascota[2].age)
            self.lblespe3.setText(listMascota[2].especie)
            self.lblraza3.setText(listMascota[2].raza)
        else:
            self.lblnom3.setText("")
            self.lblAge3.setText("")
            self.lblespe3.setText("")
            self.lblraza3.setText("")

# Configuración básica de la aplicación
app = QApplication(sys.argv)
Pet = mascotReg()
Pet.show()
app.exec()