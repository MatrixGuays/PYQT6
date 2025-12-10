import sys 
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)

class MainWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_UI()
        
    def inicializar_UI (self):
        self.setGeometry (100, 100, 500, 150)
        self.setWindowTitle ("Layouts Nested")
        self.generar_formulario()
        self.show()
        
    def generar_formulario (self):
        mensaje_principal = QLabel ("Ingresa tu informacion")
        nombres_label = QLabel ("Nombres:")
        nombres_label.setFixedWidth (60)
        self.nombres_input = QLineEdit()
        apellidos_label = QLabel ("Apellidos:")
        self.apellidos_input = QLineEdit()
        apellidos_label.setFixedWidth (60)
        edad_label = QLabel ("Edad:")
        self.edad_input = QLineEdit()
        edad_label.setFixedWidth (60)
        correo_label = QLabel ("Correo:")
        self.correo_input = QLineEdit()
        correo_label.setFixedWidth (60)
        direccion_label = QLabel ("Direccion:")
        self.direccion_input = QLineEdit()
        nombres_label.setFixedWidth (60)
        telefono_label = QLabel ("Telefono:")
        self.telefono_input = QLineEdit()
        telefono_label.setFixedWidth (60)
        enviar_button = QPushButton ("Enviar")
        
        vertical_layout_main = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()
        
        h_layout_1.addWidget (nombres_label)
        h_layout_1.addWidget (self.nombres_input)
        h_layout_1.addWidget (correo_label)
        h_layout_1.addWidget (self.correo_input)
        
        h_layout_2.addWidget (apellidos_label)
        h_layout_2.addWidget (self.apellidos_input)
        h_layout_2.addWidget (direccion_label)
        h_layout_2.addWidget (self.direccion_input)
        
        h_layout_3.addWidget (edad_label)
        h_layout_3.addWidget (self.edad_input)
        h_layout_3.addWidget (telefono_label)
        h_layout_3.addWidget (self.telefono_input)
        
        vertical_layout_main.addWidget (mensaje_principal)
        vertical_layout_main.addLayout (h_layout_1)
        vertical_layout_main.addLayout (h_layout_2)
        vertical_layout_main.addLayout (h_layout_3)
        vertical_layout_main.addWidget (enviar_button)
        
        self.setLayout (vertical_layout_main)
        
if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = MainWindow()
    sys.exit (app.exec())