from PyQt6.QtCore import QTime

def update_footer_clock(clock_label):
    """
    Aktualizuje etykietę zegara w stopce.
    Keywords: footer, clock logic, update time, PyQt6
    """
    try:
        current_time = QTime.currentTime().toString("hh:mm:ss")
        clock_label.setText(current_time)
    except Exception as e:
        print("Error updating footer clock:", e)

# Keywords: clock_logic, footer, PyQt6
