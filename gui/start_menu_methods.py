# O3ORGANIZ3R/gui/start_menu_methods.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QTimer

# Import funkcji z modułów logiki Menu Start
from gui.window_logic.start_menu.themes import toggle_dark_light
from gui.window_logic.start_menu.notifications import show_notification
from gui.window_logic.start_menu.search import perform_search
from gui.window_logic.start_menu.favorites import add_favorite
from gui.window_logic.start_menu.recent_history import get_recent_apps
from gui.window_logic.start_menu.terminal_integration import open_terminal
from gui.window_logic.start_menu.shortcuts import register_shortcuts
from gui.window_logic.start_menu.extra_features import monitor_system_resources

class StartMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        label = QLabel("Menu Start - Placeholder")
        layout.addWidget(label)
        
        # Przykładowe przyciski wywołujące funkcje logiki
        btn_theme = QPushButton("Przełącz tryb ciemny/jasny")
        btn_theme.clicked.connect(lambda: toggle_dark_light(self))
        layout.addWidget(btn_theme)
        
        btn_notification = QPushButton("Pokaż powiadomienie")
        btn_notification.clicked.connect(lambda: show_notification("To jest przykładowe powiadomienie"))
        layout.addWidget(btn_notification)
        
        btn_search = QPushButton("Wyszukaj aplikację")
        btn_search.clicked.connect(lambda: print(perform_search("Terminal")))
        layout.addWidget(btn_search)
        
        btn_fav = QPushButton("Dodaj ulubioną aplikację")
        btn_fav.clicked.connect(lambda: add_favorite("Terminal"))
        layout.addWidget(btn_fav)
        
        btn_recent = QPushButton("Pokaż ostatnio używane aplikacje")
        btn_recent.clicked.connect(lambda: print(get_recent_apps()))
        layout.addWidget(btn_recent)
        
        btn_terminal = QPushButton("Otwórz terminal")
        btn_terminal.clicked.connect(open_terminal)
        layout.addWidget(btn_terminal)
        
        # Przykładowy przycisk z modułu extra_features
        btn_extra = QPushButton("Monitoruj zasoby systemowe")
        btn_extra.clicked.connect(monitor_system_resources)
        layout.addWidget(btn_extra)
        
        self.setLayout(layout)
        
        # Rejestracja skrótów
        register_shortcuts()
        
        # Timer symulujący dynamiczne aktualizacje
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: print("[Start Menu] Aktualizacja interfejsu (placeholder)"))
        self.timer.start(5000)  # co 5 sekund

def open_start_menu():
    menu = StartMenu()
    menu.show()
