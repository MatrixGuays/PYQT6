import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QStatusBar, QFileDialog, QTextEdit, QVBoxLayout, QWidget, QFontDialog)
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtGui import QAction, QKeySequence 

class MainWindow (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.inicialize_ui()
        self.status_bar = QStatusBar()
        self.setStatusBar (self.status_bar)
        self.status_bar.setStyleSheet("BackGround-color: white;")
        
    
    def inicialize_ui (self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle ("Ventana Principal")
        self.generate_window()
        self.show()
    
    def generate_window (self):
        self.create_action()
        self.create_menu()
        self.create_content()
    
    def create_content(self):
        layout = QVBoxLayout()
        self.editor_text = QTextEdit()
        layout.addWidget (self.editor_text)
        layout.setContentsMargins(30, 30, 30, 30)
        container = QWidget()
        container.setLayout (layout)
        self.setCentralWidget (container)
    
    def create_action(self):
        self.open_action = QAction ("Abrir", self)
        self.open_action.setShortcut(QKeySequence("ctrl+O"))
        self.open_action.setStatusTip ("Abrir un archivo")
        self.open_action.triggered.connect (self.open)
        
        self.save_action = QAction ("Guardar", self)
        self.save_action.setShortcut(QKeySequence("ctrl+S"))
        self.save_action.setStatusTip ("Guardar un archivo")
        self.save_action.triggered.connect (self.save)
        
        self.export_action = QAction ("Exportar", self)
        self.export_action.setShortcut(QKeySequence("ctrl+E"))
        self.export_action.setStatusTip ("Exportar archivos")
        self.export_action.triggered.connect (self.export)
        
        self.font_action = QAction ("Fuente", self)
        self.font_action.setShortcut (QKeySequence("ctrl+F"))
        self.font_action.setStatusTip ("Cambiar Fuente")
        self.font_action.triggered.connect (self.set_font)
        
        self.undo_action = QAction ("Deshacer", self)
        self.undo_action.setShortcut (QKeySequence("ctrl+Z"))
        self.undo_action.setStatusTip ("Deshacer cambios")
        self.undo_action.triggered.connect (self.set_font)
        
        self.redo_action = QAction ("Rehacer", self)
        self.redo_action.setShortcut (QKeySequence("ctrl+Y"))
        self.redo_action.setStatusTip ("Rehacer cambios")
        self.redo_action.triggered.connect (self.redo)   
    
    def create_menu(self):
        menu_archivo = self.menuBar().addMenu ("Archivo")
        menu_archivo.addAction (self.open_action)
        menu_archivo.addAction (self.save_action)
        menu_archivo.addAction (self.export_action)
        
        menu_editar = self.menuBar().addMenu ("Editar")
        menu_editar.addAction (self.font_action)
        menu_editar.addAction (self.undo_action)
        menu_editar.addAction (self.redo_action)
    
    def open (self):
        print("Abriendo archivo...")
        options = (QFileDialog.Option.DontUseNativeDialog)
        initial_dir = QStandardPaths.writableLocation (QStandardPaths.StandardLocation.DocumentsLocation)
        file_types = "Text files (*.txt);;Imagenes (*.png);;all files (*)"
        self.file , _ =  QFileDialog.getOpenFileName(self, "Open File", initial_dir, file_types, options=options)
        
        with open(self.file, "r" ) as file:
            self.setWindowTitle(f"Ventana Activa - {self.file}")
            self.editor_text.setText (file.read())
    
    def set_font (self):
        print("Cambiando fuente...")
        selected_text_cursor = self.editor_text.textCursor()
        
        font , ok = QFontDialog.getFont(
            self.editor_text.currentFont(), self
            
        )
        
        if ok:
            if selected_text_cursor.hasSelection():
                format = self.editor_text.currentCharFormat()
                format.setFont (font)
                selected_text_cursor.mergeCharFormat (format)
            else:
                self.editor_text.setCurrentFont (font)
    
    def save (self):
        print("Guardando archivo...")
    
    def export (self):
        print("Exportando archivo...")
    
    def undo (self):
        print("Deshaciendo Cambios...")
    
    def redo (self):
        print("Rehaciendo Cambios...")

if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = MainWindow()
    sys.exit (app.exec())