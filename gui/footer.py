# /home/dev/Desktop/o3organiz3r/gui/footer.py

import os
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer, Qt
from gui.window_logic.footer.footer_methods import activate_footer_menu, update_footer_display

class Footer(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.initUI()
        except Exception as e:
            print("Error initializing Footer UI:", e)
    
    def initUI(self):
        try:
            # Główny layout stopki – poziomy
            main_layout = QHBoxLayout()
            
            # Lewa część stopki – przycisk dynamicznego menu (wcześniej Settings)
            left_layout = QHBoxLayout()
            btn_menu = QPushButton("")
            # Używamy ikony z katalogu resources (możesz zmienić ikonę na bardziej pasującą do "menu")
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
            menu_icon_path = os.path.join(base_dir, "resources", "settings_icon_1616.jpg")
            btn_menu.setIcon(QIcon(menu_icon_path))
            btn_menu.setFixedSize(30, 30)
            # Po kliknięciu przycisk wywołuje funkcję dynamicznego menu
            btn_menu.clicked.connect(lambda: activate_footer_menu(self))
            left_layout.addWidget(btn_menu)
            
            btn_exit = QPushButton("Exit")
            btn_exit.clicked.connect(lambda: exit_app_footer(self))
            left_layout.addWidget(btn_exit)
            
            # Lewy kontener – wyrównujemy do lewej
            left_container = QWidget()
            left_container.setLayout(left_layout)
            main_layout.addWidget(left_container, alignment=Qt.AlignmentFlag.AlignLeft)
            
            # Prawa część stopki – kontener z zegarem i kalendarzem (widoczny na stałe)
            right_layout = QVBoxLayout()
            self.clock_label = QLabel("00:00:00")
            self.clock_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.date_label = QLabel("yyyy-mm-dd")
            self.date_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            right_layout.addWidget(self.clock_label)
            right_layout.addWidget(self.date_label)
            
            right_container = QWidget()
            right_container.setLayout(right_layout)
            main_layout.addWidget(right_container, alignment=Qt.AlignmentFlag.AlignRight)
            
            self.setLayout(main_layout)
            
            # Inicjalizacja logiki backendu stopki (aktualizacja daty i godziny)
            # (Funkcja activate_footer_menu będzie wywoływana po kliknięciu przycisku)
            
            # Ustawienie timera do aktualizacji zegara i daty w stopce
            self.timer = QTimer(self)
            self.timer.timeout.connect(lambda: update_footer_display(self))
            self.timer.start(1000)  # Aktualizacja co sekundę
        except Exception as e:
            print("Error in Footer initUI:", e)

# Funkcja exit_app_footer – nie modyfikujemy jej, pozostaje taka sama
def exit_app_footer(widget):
    from PyQt6.QtWidgets import QMessageBox, QApplication
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
        print("Error in exit_app_footer:", e)
