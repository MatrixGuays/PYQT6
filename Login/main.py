from PyQt6.QtWidgets import (QWidget, QLabel, QMessageBox)
from PyQt6.QtGui import QPixmap

class mainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui (self):
        self.setGeometry (100, 100, 400, 300)
        self.setWindowTitle ("Imagen")
        self.generar_contenido()
    
    def generar_contenido (self):
        image_path = "ciudad.png"
        
        try:
            with open (image_path):
                pixmap = QPixmap()
                image_label = QLabel (self)
                image_label.setPixmap (QPixmap(image_path))

        except FileNotFoundError as e:
            QMessageBox.warning (self, "Error", "No se encontro la imagen: {e}", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        
        except Exception as e:
            QMessageBox.warning (self, "Error", "Error en el main view: {e}", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)