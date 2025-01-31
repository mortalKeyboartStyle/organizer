import logging
from PyQt6.QtCore import QDateTime

class FooterMethods:
    """
    Klasa z metodami obsługującymi logikę stopki:
      - on_prev_page_clicked
      - on_next_page_clicked
      - update_clock
    """

    def on_prev_page_clicked(self):
        """
        Placeholder: w tym momencie QToolBox nie ma 'poprzedniej' czy 'następnej' strony.
        Docelowo można tu przełączać QStackedWidget.setCurrentIndex(...)
        """
        logging.info("Kliknięto 'Poprzednia strona' - footer method placeholder.")

    def on_next_page_clicked(self):
        """
        Placeholder: analogicznie, docelowo do obsługi wielostronicowego interfejsu.
        """
        logging.info("Kliknięto 'Następna strona' - footer method placeholder.")

    def update_clock(self):
        """
        Aktualizuje zegar w stopce, np. co 1 sek. wywoływane przez QTimer.
        """
        now = QDateTime.currentDateTime()
        time_str = now.toString("yyyy-MM-dd HH:mm:ss")
        self.clock_label.setText(time_str)
