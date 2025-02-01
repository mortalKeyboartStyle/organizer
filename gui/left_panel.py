from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.window_logic.left_menu_methods import init_left_menu_logic

class LeftPanel(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.initUI()
        except Exception as e:
            print("Error in LeftPanel initialization:", e)
    
    def initUI(self):
        try:
            layout = QVBoxLayout()
            layout.addWidget(QLabel("Lewy Panel - Placeholder"))
            self.setLayout(layout)
            self.setFixedWidth(450)
            init_left_menu_logic(self)
        except Exception as e:
            print("Error in LeftPanel initUI:", e)

# Keywords: left panel, UI, fixed width, PyQt6
