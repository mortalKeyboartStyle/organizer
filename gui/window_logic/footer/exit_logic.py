from PyQt6.QtWidgets import QMessageBox, QApplication

def exit_application(widget):
    """
    Kończy działanie aplikacji po potwierdzeniu.
    """
    try:
        reply = QMessageBox.question(
            widget,
            "Confirm Exit",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()
    except Exception as e:
        print("Error in footer exit_logic:", e)

# Keywords: footer exit logic, quit application, PyQt6
