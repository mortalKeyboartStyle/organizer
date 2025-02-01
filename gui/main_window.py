# /home/dev/Desktop/o3organiz3r/gui/main_window.py

from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QFrame
from gui.left_panel import LeftPanel
from gui.right_panel import RightPanel
from gui.footer import Footer
from program_logic.settings import CURRENT_STYLE
from gui.window_logic.main_window_methods import apply_main_window_logic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            self.setWindowTitle("O3organiz3r - 8-bit Style GUI")
            self.setGeometry(100, 100, 800, 600)
            self.setStyleSheet(CURRENT_STYLE)
            self.initUI()
        except Exception as e:
            print("Error in MainWindow initialization:", e)
    
    def initUI(self):
        try:
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
            
            main_layout = QVBoxLayout()
            content_layout = QHBoxLayout()
            
            self.left_panel = LeftPanel()
            self.left_panel.setFixedWidth(450)  # Lewy panel na 450 px od lewego marginesu
            content_layout.addWidget(self.left_panel)
            
            # Separator pionowy
            v_line = QFrame()
            v_line.setFrameShape(QFrame.Shape.VLine)
            v_line.setFrameShadow(QFrame.Shadow.Sunken)
            content_layout.addWidget(v_line)
            
            self.right_panel = RightPanel()
            content_layout.addWidget(self.right_panel)
            
            main_layout.addLayout(content_layout)
            
            # Separator poziomy przed stopką
            h_line = QFrame()
            h_line.setFrameShape(QFrame.Shape.HLine)
            h_line.setFrameShadow(QFrame.Shadow.Sunken)
            main_layout.addWidget(h_line)
            
            self.footer = Footer()
            self.footer.setFixedHeight(100)  # Stopka 100 px od dołu
            main_layout.addWidget(self.footer)
            
            central_widget.setLayout(main_layout)
            
            apply_main_window_logic(self)
        except Exception as e:
            print("Error in MainWindow initUI:", e)
