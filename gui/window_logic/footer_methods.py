from PyQt6.QtWidgets import QMessageBox, QApplication
from gui.clock_dialog import ClockDialog
from gui.calendar_dialog import CalendarDialog

def init_footer_logic(footer_instance):
    """
    Dodatkowa inicjalizacja logiki dla stopki (mini-tray).
    
    Keywords: footer, initialization, logic, PyQt6
    """
    try:
        print("Footer tray logic initialized.")
    except Exception as e:
        print("Error in init_footer_logic:", e)

def show_clock_footer(footer_instance):
    """
    Otwiera dialog zegara.
    
    Keywords: clock, dialog, footer, logic, PyQt6
    """
    try:
        clock_dialog = ClockDialog()
        clock_dialog.show()
    except Exception as e:
        print("Error in show_clock_footer:", e)

def show_calendar_footer(footer_instance):
    """
    Otwiera dialog kalendarza.
    
    Keywords: calendar, dialog, footer, logic, PyQt6
    """
    try:
        calendar_dialog = CalendarDialog()
        calendar_dialog.show()
    except Exception as e:
        print("Error in show_calendar_footer:", e)

def open_settings_footer(footer_instance):
    """
    Placeholder – otwiera okno ustawień lub wyświetla komunikat.
    
    Keywords: settings, dialog, footer, logic, PyQt6
    """
    try:
        QMessageBox.information(footer_instance, "Settings", "Settings dialog not implemented yet.")
    except Exception as e:
        print("Error in open_settings_footer:", e)

def exit_app_footer(footer_instance):
    """
    Zamyka aplikację po potwierdzeniu.
    
    Keywords: exit, application, footer, logic, PyQt6
    """
    try:
        reply = QMessageBox.question(
            footer_instance,
            "Confirm Exit",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()
    except Exception as e:
        print("Error in exit_app_footer:", e)

# Keywords: footer_methods, logic, error handling, PyQt6
