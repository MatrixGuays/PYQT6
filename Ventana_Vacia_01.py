import sys 
from PyQt6.QtWidgets import QApplication, QWidget

class ventana_vacia(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializarUI() 
        
    def inicializarUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Ventana Vacía")
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ventana_vacia()
    sys.exit(app.exec())