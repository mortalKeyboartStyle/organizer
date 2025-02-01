from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel
from gui.window_logic.clock_dialog_methods import update_time_logic
from PyQt6.QtCore import QTimer

class ClockDialog(QDialog):
    def __init__(self):
        super().__init__()
        try:
            self.setWindowTitle("Zegar")
            self.initUI()
        except Exception as e:
            print("Error in ClockDialog initialization:", e)
    
    def initUI(self):
        try:
            self.layout = QVBoxLayout()
            self.label = QLabel()
            self.layout.addWidget(self.label)
            self.setLayout(self.layout)
            
            self.timer = QTimer(self)
            self.timer.timeout.connect(lambda: update_time_logic(self))
            self.timer.start(1000)
            update_time_logic(self)
        except Exception as e:
            print("Error in ClockDialog initUI:", e)

# Keywords: clock dialog, UI, timer, PyQt6
