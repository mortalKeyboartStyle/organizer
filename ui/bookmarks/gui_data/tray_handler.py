"""
tray_handler.py
Keyword: gui_data_tray

Aplikacja w zasobniku systemowym, pokazuje powiadomienia.
Wymaga QSystemTrayIcon (PyQt6).
"""

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu

def enable_system_tray(main_window, icon_path="icon.png"):
    """
    Uruchamia tray icon, pozwala minimalizować do traya.
    """
    tray_icon = QSystemTrayIcon(QIcon(icon_path), main_window)
    tray_menu = QMenu()
    
    restore_action = tray_menu.addAction("Przywróć okno")
    quit_action = tray_menu.addAction("Zamknij")

    restore_action.triggered.connect(main_window.showNormal)
    quit_action.triggered.connect(main_window.close)

    tray_icon.setContextMenu(tray_menu)
    tray_icon.setToolTip("WyszukiwaczPromocji - Działa w tle")
    tray_icon.show()

    main_window.tray_icon = tray_icon  # zachowujemy referencję, aby nie zginęło
