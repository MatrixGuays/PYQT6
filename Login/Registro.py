from PyQt6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit, QMessageBox)
from PyQt6.QtGui import QFont

class RegistrarUsuarioView(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.generar_formulario()
        
    def generar_formulario(self):
        self.setGeometry (100, 100, 350, 250)
        self.setWindowTitle ("Registro de Windows")
        
        user_label = QLabel (self)
        user_label.setText ("Usuario: ")
        user_label.setFont (QFont("Arial", 10))
        user_label.move (20, 44)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize (250, 24)
        self.user_input.move (90, 40)
        
        Password_1_label = QLabel(self)
        Password_1_label.setText ("Password: ")
        Password_1_label.setFont (QFont("Arial", 10))
        Password_1_label.move (20, 84)
        
        self.Password_1_input = QLineEdit(self)
        self.Password_1_input.resize(250, 24)
        self.Password_1_input.move(90, 80)
        self.Password_1_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        Password_2_label = QLabel (self)
        Password_2_label.setText ("confirmar ")
        Password_2_label.setFont (QFont("Arial", 10))
        Password_2_label.move (20, 125)
        
        self.Password_2_input = QLineEdit(self)
        self.Password_2_input.resize (250, 24)
        self.Password_2_input.move (90, 120)
        self.Password_2_input.setEchoMode (QLineEdit.EchoMode.Password)
        
        create_button = QPushButton (self)
        create_button.setText ("Crear Usuario")
        create_button.resize (150, 32)
        create_button.move (20, 170)
        create_button.clicked.connect (self.crear_usuario)

        cancel_button = QPushButton (self)
        cancel_button.setText ("Cancelar")
        cancel_button.resize (150, 32)
        cancel_button.move (170, 170)
        cancel_button.clicked.connect(self.cancelar_creacion)
        
    def cancelar_creacion(self):
        self.close()
        
    def crear_usuario(self):
        User_path  = "usuarios.txt"
        usuario = self.user_input.text()
        password_1 = self.Password_1_input.text()   
        password_2 = self.Password_2_input.text()
        
        if password_1 == "" or  password_2 == "" or usuario == "":
            QMessageBox.warning (self, "Error", "Por favor complete todos los campos", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        
        elif password_1 != password_2:
            QMessageBox.warning (self, "Error", "Las contraseñas no coinciden", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            
        else:
            try:
                with open (User_path, "a+") as f:
                    f.write (f"{usuario},{password_1}\n")
                QMessageBox.information (self, "Éxito", "Usuario creado con exito", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                self.close()
            except FileNotFoundError as e:
                QMessageBox.warning (self, "Error", f"La base de datos no existe{e}", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)