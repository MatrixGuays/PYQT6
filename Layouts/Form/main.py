import sys
from PyQt6. QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QDateEdit, QLineEdit, QComboBox, QFormLayout, QHBoxLayout, QMessageBox)
from PyQt6.QtGui import QFont 
from PyQt6.QtCore import Qt, QDate 

class MainWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.inicialize_ui()
        
    def inicialize_ui(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("Formulario de Registro")
        self.crear_formulario()
        self.show()
        
    def crear_formulario(self):
        titulo = QLabel ("Solicitud de Ingreso")
        titulo.setFont(QFont("Arial", 18))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)       
        
        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Nombre")   
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Apellido")   
        
        self.genero_selection = QComboBox()
        self.genero_selection.addItems (["Masculino", "Femenino", "Otro"])
        
        self.fecha_nacimiento_edit = QDateEdit()
        self.fecha_nacimiento_edit.setDisplayFormat("yyyy-mm-dd")
        self.fecha_nacimiento_edit.setMaximumDate(QDate.currentDate())
        
        self.fecha_nacimiento_edit.setCalendarPopup(True)
        self.fecha_nacimiento_edit.setDate(QDate.currentDate())
        
        self.telefono = QLineEdit()
        self.telefono.setPlaceholderText("123-456-7890")
        
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.mostrar_info)
        
        primer_h_box = QHBoxLayout()
        primer_h_box.addWidget(self.nombre_edit)
        primer_h_box.addWidget(self.apellido_edit)
        
        main_form = QFormLayout()
        main_form.addRow(titulo)
        main_form.addRow("Nombre y Apellido:", primer_h_box)
        main_form.addRow("Genero:", self.genero_selection)
        main_form.addRow("Fecha de Nacimiento:", self.fecha_nacimiento_edit)
        main_form.addRow("Telefono:", self.telefono)
        main_form.addRow(submit_button)
        
        self.setLayout(main_form)
        
    def mostrar_info(self):
        QMessageBox.information(self, "Informacion de Registro",
        f"Nombre: {self.nombre_edit.text()} {self.apellido_edit.text()} \n \ Genero: {self.genero_selection.currentText()} \n \ fecha de Nacimiento: {self.fecha_nacimiento_edit.text()} \n \ telefono: {self.telefono.text()}", QMessageBox.StardardButton.Ok, QMessageBox.StandardButton.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())

