import sys 
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout)
import operator

operation = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
        self.primer_valor = ""
        self.segundo_valor = ""
        self.operador = ""
        self.pointer_flag = "1"
        self.after_equal = False
        self.after_operator = False

    def inicializar_ui(self):
        self.setWindowTitle("Calculadora Simple")
        self.setGeometry(100, 100, 600, 400)
        self.generar_interfaz()
        self.show()
        
    def generar_interfaz(self):
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(True)
        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_00 = QPushButton("00")
        boton_punto = QPushButton(".")
        
        boton_1.clicked.connect(self.ingresar_datos)
        boton_2.clicked.connect(self.ingresar_datos)
        boton_3.clicked.connect(self.ingresar_datos)
        boton_4.clicked.connect (self.ingresar_datos)
        boton_5.clicked.connect(self.ingresar_datos)
        boton_6.clicked.connect(self.ingresar_datos)
        boton_7.clicked.connect(self.ingresar_datos)
        boton_8.clicked.connect(self.ingresar_datos)
        boton_9.clicked.connect(self.ingresar_datos)
        boton_0.clicked.connect(self.ingresar_datos)
        boton_00.clicked.connect(self.ingresar_datos)
        boton_punto.clicked.connect(self.ingresar_datos)
        
        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("*")
        boton_division = QPushButton("/")
        
        boton_suma.clicked.connect(self.insertar_operador)
        boton_resta.clicked.connect(self.insertar_operador)
        boton_multiplicacion.clicked.connect(self.insertar_operador)
        boton_division.clicked.connect(self.insertar_operador)
        
        boton_CE = QPushButton("CE")
        boton_CE.clicked.connect(self.borrar_todo)
        boton_borrar = QPushButton("⌫")
        boton_borrar.clicked.connect(self.borrar_parcial)
        boton_resultado = QPushButton("=")
        boton_resultado.clicked.connect(self.calcular_operacion)
        
        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla, 0, 0, 2, 4)
        self.main_grid.addWidget(boton_CE, 2, 0, 1, 2)
        self.main_grid.addWidget(boton_borrar, 2, 2)
        self.main_grid.addWidget(boton_suma, 2, 3)
        
        self.main_grid.addWidget(boton_7, 3, 0)
        self.main_grid.addWidget(boton_8, 3, 1)
        self.main_grid.addWidget(boton_9, 3, 2)
        self.main_grid.addWidget(boton_division, 3, 3)
        
        self.main_grid.addWidget(boton_4, 4, 0)
        self.main_grid.addWidget(boton_5, 4, 1)
        self.main_grid.addWidget(boton_6, 4, 2)
        self.main_grid.addWidget(boton_multiplicacion, 4, 3)
        
        self.main_grid.addWidget(boton_1, 5, 0)
        self.main_grid.addWidget(boton_2, 5, 1) 
        self.main_grid.addWidget(boton_3, 5, 2)
        self.main_grid.addWidget(boton_resta, 5, 3)
        
        self.main_grid.addWidget(boton_0, 6, 0)
        self.main_grid.addWidget(boton_00, 6, 1)
        self.main_grid.addWidget(boton_punto, 6, 2)
        self.main_grid.addWidget(boton_resultado, 6, 3)
        
        self.setLayout(self.main_grid)
    
    def ingresar_datos (self):
        boton_text = self.sender().text()
        if self.after_equal:
            self.primer_valor = ""
            self.pantalla.setText(self.primer_valor)
            self.after_equal = False
            self.pointer_flag = "1"
            
        if self.pointer_flag == "1":
            self.primer_valor += boton_text
            self.pantalla.setText(self.primer_valor)
            
        else:
            self.segundo_valor += boton_text
            self.pantalla.setText(self.pantalla.toPlainText() + boton_text)
            self.after_operator = False
            
        
            

    def insertar_operador (self):
        boton_text = self.sender().text()
        self.operador = boton_text
        self.pointer_flag = "2"
        
        if self.after_operator == True:
            self.calcular_operacion()
            self.pantalla.setText(self.primer_valor + " " + self.operador + " " )
            self.after_operator = False
        else:
            self.pantalla.setText(self.pantalla.toPlainText() + " " + self.operador + " ")
        self.after_operator = True 
        self.after_equal = False
    
    def borrar_todo (self):
        self.primer_valor = ""
        self.segundo_valor = ""
        self.operador = ""
        self.pointer_flag = "1"
        self.after_equal = False
        self.after_operator = False
        self.pantalla.setText("")
        
    def borrar_parcial (self):
        if self.after_equal:
            self.borrar_todo()
            
        if self.pointer_flag == "1":
            self.primer_valor = self.primer_valor[:-1]
            self.pantalla.setText(self.primer_valor)
        else:
            self.segundo_valor = self.segundo_valor[:-1]
            self.pantalla.setText(self.segundo_valor)
            
    def calcular_operacion (self):
        resultado = str(operation[self.operador](float(self.primer_valor), float(self.segundo_valor)))
        self.pantalla.setText(resultado)
        self.primer_valor = resultado
        self.segundo_valor = ""
        self.after_equal = True
        self.after_operator = False 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Windows = MainWindow()
    sys.exit(app.exec())