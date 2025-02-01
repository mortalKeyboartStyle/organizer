import os
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu, QMessageBox, QApplication
from PyQt6.QtGui import QAction, QIcon
from gui.clock_dialog import ClockDialog
from gui.calendar_dialog import CalendarDialog
from gui.window_logic.tray_methods import show_clock_logic, show_calendar_logic, exit_app_logic, init_tray_menu_logic

class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        try:
            # Ładowanie ikony tray z katalogu resources
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
            tray_icon_path = os.path.join(base_dir, "resources", "tray_icon.png")
            icon = QIcon(tray_icon_path)
        except Exception as e:
            print("Błąd przy ładowaniu ikony tray:", e)
            icon = QIcon()
        super().__init__(icon, parent)
        try:
            self.setToolTip("O3organiz3r Tray")
            self.parent = parent
            self.initTrayMenu()  # Inicjalizacja menu tray
        except Exception as e:
            print("Błąd przy inicjalizacji TrayIcon:", e)

    def initTrayMenu(self):
        try:
            self.menu = QMenu()
            # Akcja: Pokaż Zegar – delegacja logiki do tray_methods
            self.action_clock = QAction("Pokaż Zegar", self)
            self.action_clock.triggered.connect(lambda: show_clock_logic(self))
            self.menu.addAction(self.action_clock)

            # Akcja: Pokaż Kalendarz – delegacja logiki do tray_methods
            self.action_calendar = QAction("Pokaż Kalendarz", self)
            self.action_calendar.triggered.connect(lambda: show_calendar_logic(self))
            self.menu.addAction(self.action_calendar)

            self.menu.addSeparator()

            # Akcja: Wyjdź z aplikacji – delegacja logiki do tray_methods
            self.action_exit = QAction("Wyjdź", self)
            self.action_exit.triggered.connect(lambda: exit_app_logic(self))
            self.menu.addAction(self.action_exit)

            # Dodatkowa inicjalizacja logiki tray (opcjonalna)
            init_tray_menu_logic(self)
            self.setContextMenu(self.menu)
        except Exception as e:
            print("Błąd przy inicjalizacji menu tray:", e)

# Keywords: tray, system tray, UI, separation, PyQt6
