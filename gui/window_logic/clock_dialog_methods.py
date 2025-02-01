from PyQt6.QtCore import QTime

def update_time_logic(clock_dialog_instance):
    """
    Aktualizuje wyświetlany czas w dialogu zegara.
    """
    try:
        current_time = QTime.currentTime().toString("hh:mm:ss")
        clock_dialog_instance.label.setText("Aktualny czas: " + current_time)
    except Exception as e:
        print("Error updating time in ClockDialog:", e)

# Keywords: clock logic, update time, PyQt6
