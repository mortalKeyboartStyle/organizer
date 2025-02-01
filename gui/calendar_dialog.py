from PyQt6.QtWidgets import QDialog, QVBoxLayout, QCalendarWidget
from gui.window_logic.calendar_dialog_methods import init_calendar_logic

class CalendarDialog(QDialog):
    def __init__(self):
        super().__init__()
        try:
            self.setWindowTitle("Kalendarz")
            self.initUI()
        except Exception as e:
            print("Błąd w inicjalizacji CalendarDialog:", e)

    def initUI(self):
        try:
            self.layout = QVBoxLayout()
            self.calendar = QCalendarWidget()
            self.layout.addWidget(self.calendar)
            self.setLayout(self.layout)
            init_calendar_logic(self)
        except Exception as e:
            print("Błąd w metodzie initUI CalendarDialog:", e)

# Keywords: calendar_dialog, UI, separation, PyQt6
