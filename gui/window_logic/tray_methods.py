from PyQt6.QtWidgets import QApplication, QMessageBox
from gui.clock_dialog import ClockDialog
from gui.calendar_dialog import CalendarDialog

def init_tray_menu_logic(tray_instance):
    """
    Dodatkowa inicjalizacja logiki dla menu tray.
    Keywords: tray, initialization, logic, PyQt6
    """
    try:
        # Możliwość dodania dodatkowych operacji inicjalizacyjnych
        print("Tray menu logic initialized")
    except Exception as e:
        print("Błąd w init_tray_menu_logic:", e)

def show_clock_logic(tray_instance):
    """
    Logika wyświetlania dialogu zegara.
    Keywords: clock, dialog, tray, logic, PyQt6
    """
    try:
        clock_dialog = ClockDialog()
        clock_dialog.show()
    except Exception as e:
        print("Błąd w show_clock_logic:", e)

def show_calendar_logic(tray_instance):
    """
    Logika wyświetlania dialogu kalendarza.
    Keywords: calendar, dialog, tray, logic, PyQt6
    """
    try:
        calendar_dialog = CalendarDialog()
        calendar_dialog.show()
    except Exception as e:
        print("Błąd w show_calendar_logic:", e)

def exit_app_logic(tray_instance):
    """
    Logika zakończenia aplikacji.
    Keywords: exit, application, tray, logic, PyQt6
    """
    try:
        reply = QMessageBox.question(
            None,
            'Potwierdzenie',
            "Czy na pewno chcesz zakończyć aplikację?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            tray_instance.hide()
            QApplication.quit()
    except Exception as e:
        print("Błąd w exit_app_logic:", e)

# Keywords: tray_methods, logic, separation, PyQt6
