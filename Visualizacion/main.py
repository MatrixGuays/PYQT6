import sys 
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QDockWidget, QStatusBar, QTabWidget, QWidget, QHBoxLayout, QVBoxLayout, QListWidget)

from PyQt6.QtGui import QPixmap, QAction, QKeySequence
from PyQt6.QtCore import Qt

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
    
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
        buttons_repeat = QPushButton("🚨")
        buttons_before = QPushButton("🏛")
        buttons_play = QPushButton ("💵")
        buttons_next = QPushButton("🛠")
        buttons_radom = QPushButton ("📍")
        
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
    
    #MENU
    def create_menu(self):
        self.menuBar()
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
