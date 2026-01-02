import sys 
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QDockWidget, QStatusBar, QTabWidget, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QFileDialog, QListWidgetItem)

from PyQt6.QtGui import QPixmap, QAction, QKeySequence, QIcon
from PyQt6.QtCore import Qt, QStandardPaths, QSize

class MainWindow (QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        with open("estilos.css", "r") as file:
            style = file.read()
        self.setStyleSheet(style)
    
    def initialize_ui(self):
        self.setGeometry (100, 100, 800, 500)
        self.setWindowTitle("Visualizador")
        self.generate_main_window()
        self.create_action()
        self.create_menu()
        self.create_dock()
        self.show()
    def generate_main_window(self):
        tab_bar = QTabWidget(self)
        self.reproductor_container = QWidget()
        self.settings_container = QWidget()
        tab_bar.addTab(self.reproductor_container, "Visualizador")
        
        tab_bar.addTab(self.settings_container, "settings")
        
        self.generate_reproductor_tab()
        self.generate_settings_tab()
        
        tab_h_box = QHBoxLayout()
        tab_h_box.addWidget(tab_bar)
        
        main_container = QWidget()
        main_container.setLayout(tab_h_box)
        self.setCentralWidget(main_container)
    
    def generate_reproductor_tab(self):
        main_v_box = QVBoxLayout()
        buttons_h_box = QHBoxLayout()
        
        #imagen
        song_image = QLabel()
        pixmap = QPixmap("Images/Beige.jpg")
        song_image.setPixmap(pixmap)
        song_image.setScaledContents(True)
        
        #botones
        buttons_repeat = QPushButton()
        buttons_repeat.setObjectName("buttons_repeat")
        buttons_repeat.setIcon(QIcon("Images/repeat.png"))
        buttons_repeat.setIconSize(QSize(24, 24))
        buttons_before = QPushButton()
        buttons_before.setObjectName("buttons_before")
        buttons_before.setIcon(QIcon("Images/izquierda.png"))
        buttons_before.setIconSize(QSize(24, 24))
        buttons_play = QPushButton ()
        buttons_play.setObjectName("buttons_play")
        buttons_play.setIcon(QIcon("Images/play.jpeg"))
        buttons_play.setIconSize(QSize(34, 24))
        buttons_next = QPushButton()
        buttons_next.setObjectName("buttons_next")
        buttons_next.setIcon(QIcon("Images/siguiente.jpeg"))
        buttons_next.setIconSize(QSize(24, 24))
        buttons_radom = QPushButton()
        buttons_radom.setObjectName("buttons_radom")
        buttons_radom.setIcon(QIcon("Images/random.jpeg"))
        buttons_radom.setIconSize(QSize(24, 24))
        
        
        buttons_repeat.setFixedSize(40, 40)
        buttons_before.setFixedSize (40, 40)
        buttons_play.setFixedSize(50, 50)
        buttons_next.setFixedSize(40, 40)
        buttons_radom.setFixedSize(40, 40)
        
        buttons_h_box.addWidget(buttons_repeat)
        buttons_h_box.addWidget(buttons_before)
        buttons_h_box.addWidget(buttons_play)
        buttons_h_box.addWidget(buttons_next)
        buttons_h_box.addWidget(buttons_radom)
        
        buttons_container = QWidget()
        buttons_container.setLayout(buttons_h_box)
        
        #DEMAS
        main_v_box.addWidget(song_image)
        main_v_box.addWidget(buttons_container)
        
        self.reproductor_container.setLayout(main_v_box)
        
    def create_action(self):
        self.listar_musica_action = QAction("ListarNombres", self, checkable= True)
        self.listar_musica_action.setShortcut(QKeySequence("ctrl + L"))
        self.listar_musica_action.setStatusTip("Aqui pudes listar los feriantes")
        self.listar_musica_action.triggered.connect(self.list_music)
        self.listar_musica_action.setChecked(True)
        
        self.open_folder_music_action = QAction("Abrir carpeta", self)
        self.open_folder_music_action.setShortcut(QKeySequence("ctrl+o"))
        self.open_folder_music_action.setStatusTip("Abre la carpeta")
        self.open_folder_music_action.triggered.connect(self.open_folder_music)
    
    #MENU
    def create_menu(self):
        self.menuBar()
        menu_file = self.menuBar().addMenu("File")
        menu_file.addAction(self.open_folder_music_action)
        
        menu_view = self.menuBar().addMenu("view")
        menu_view.addAction(self.listar_musica_action)
    
    def create_dock(self):
        self.songs_list = QListWidget()
        self.dock = QDockWidget()
        self.dock.setWindowTitle("Lista de Nombres")
        self.dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        self.dock.setWidget(self.songs_list)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
    
    def list_music(self):
        if self.listar_musica_action.isChecked():
            self.dock.show()
        else:
            self.dock.hide()
    
    def generate_settings_tab(self):
        pass
    
    def open_folder_music(self):
        initial_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.MusicLocation)
        selected_folder = QFileDialog.getExistingDirectory(None, "selecciona una carpeta", initial_dir)
        icon = QIcon("Images/image.png")
        
        for archivo in os.listdir(selected_folder):
            ruta_archivo = os.path.join (selected_folder, archivo)
            if ruta_archivo.endswith(".txt"):
                item = QListWidgetItem(archivo)
                item.setIcon(icon)
                self.songs_list.addItem(item)
                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
