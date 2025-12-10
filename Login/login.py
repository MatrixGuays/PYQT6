import sys 
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from Registro import RegistrarUsuarioView
from main import mainWindow


class Login(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui (self):
        self.setGeometry (100, 100, 300, 200)
        self.setWindowTitle ("Login")
        self.generar_formulario()
        self.show()
        
    def generar_formulario (self):
        self.is_logged = False
        
        user_label = QLabel (self)
        user_label.setText ("Usuario: ")
        user_label.setFont (QFont ("Arial", 10))
        user_label.move (20, 54)
        
        self.user_input = QLineEdit (self)
        self.user_input.resize (250, 24)
        self.user_input.move (90, 50)
        
        password_label = QLabel (self)
        password_label.setText ("password: ")
        password_label.setFont (QFont("Arial", 10))
        password_label.move (20, 86)
        
        self.password_input = QLineEdit (self)
        self.password_input.resize (250, 24)
        self.password_input.move (90, 82)
        self.password_input.setEchoMode (QLineEdit.EchoMode.Password)
        
        self.check_view_password = QCheckBox (self)
        self.check_view_password.setText ("Ver contraseña")
        self.check_view_password.move (90, 110)
        self.check_view_password.toggled.connect (self.mostrar_contrasena)
        
        
        login_button = QPushButton (self)
        login_button.setText ("Login")
        login_button.resize (320, 24)
        login_button.move (20, 140)
        login_button.clicked.connect (self.login)
        
        register_button = QPushButton (self)
        register_button.setText ("Register")
        register_button.resize (320, 24)
        register_button.move (20, 170)
        register_button.clicked.connect (self.registrar_usuario)
        
    def mostrar_contrasena (self, clicked):
        
        if clicked:
            self.password_input.setEchoMode (QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode (QLineEdit.EchoMode.Password)
    
    def login (self):
        user = []
        user_path = "usuarios.txt"
        
        try:
            with open (user_path, "r") as f:
                for linea in  f:
                    user.append (linea.strip("\n"))
                    login_information = f"{self.user_input.text()},{self.password_input.text()}"
                    if login_information in user:
                        self.is_logged = True
                        QMessageBox.information (self, "Exito", "Login exitoso", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                        self.close()
                        self.open_main_window()
                    else:
                        QMessageBox.warning (self, "Error", "Usuario o contraseña incorrecta", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            
            
        except FileNotFoundError as e:
            QMessageBox.warning (self, "Error", "No se encontro el usuario: ", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        
        except Exception as e:
            QMessageBox.warning (self, "Error", "error en el servidor ", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        
    def registrar_usuario (self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()
        
    def open_main_window (self):
        self.main_window = mainWindow()
        self.main_window.show()


if __name__ == "__main__":
    app = QApplication (sys.argv)
    login = Login()
    sys.exit(app.exec())