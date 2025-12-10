import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,QMessageBox)

class MainWindow (QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializar_UI()
        
    def inicializar_UI (self):
        self.setMinimumWidth (500)
        self.setFixedHeight (200)
        self.setWindowTitle ("Layout Vertical")
        self.generar_formulario()
        self.show()
        
    def generar_formulario (self):
        
        boton1 = QPushButton ("Mantenimiento")
        boton2 = QPushButton ("Reparacion")
        boton3 = QPushButton ("Organizacion")
        boton4 = QPushButton ("Practicas")
        
        boton1.clicked.connect(self.imprimir_nombre_boton)
        boton2.clicked.connect(self.imprimir_nombre_boton)
        boton3.clicked.connect(self.imprimir_nombre_boton)
        boton4.clicked.connect(self.imprimir_nombre_boton)
        
        layout = QVBoxLayout()
        layout.addWidget (boton1)
        layout.addWidget (boton2)
        layout.addWidget (boton3)
        layout.addWidget (boton4)
        self.setLayout (layout)
        
    def imprimir_nombre_boton (self):
        boton = self.sender()
        QMessageBox.information (self, "Boton presionado", f"Has presionado el boton: {boton.text()}")
        print (f"Has presionado el boton: {boton.text()}")
        
if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = MainWindow()
    sys.exit (app.exec())