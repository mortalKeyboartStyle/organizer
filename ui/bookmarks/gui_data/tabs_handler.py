"""
tabs_handler.py
Keyword: gui_data_tabs

Możliwość tworzenia osobnych zakładek dla różnych źródeł / kategorii / dni.
Prosta funkcja: add_new_tab(main_window, tab_name).
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

def add_new_tab(main_window, tab_name):
    """
    Dodaje nową zakładkę w main_window.tabs z etykietą 'tab_name'.
    Zawartość przykładowa (tylko Label).
    """
    new_tab = QWidget()
    layout = QVBoxLayout(new_tab)
    label = QLabel(f"Zakładka: {tab_name}")
    layout.addWidget(label)
    new_tab.setLayout(layout)

    main_window.tabs.addTab(new_tab, tab_name)
