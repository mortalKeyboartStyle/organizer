from PyQt6.QtCore import QDate

def update_footer_calendar(date_label):
    """
    Aktualizuje etykietę daty w stopce.
    Keywords: footer, calendar logic, update date, PyQt6
    """
    try:
        current_date = QDate.currentDate().toString("dddd, dd MMMM yyyy")
        date_label.setText(current_date)
    except Exception as e:
        print("Error updating footer calendar:", e)

# Keywords: calendar_logic, footer, PyQt6
