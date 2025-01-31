"""
kiosk_mode.py
Keyword: gui_data_kiosk

Minimalistyczny interfejs z ograniczoną liczbą przycisków.
Możemy przełączyć MainWindow w tryb kiosk (fullscreen, ukryte menu).
"""

def enable_kiosk_mode(main_window):
    """
    Ustawia okno w tryb fullscreen, ukrywa pewne elementy.
    """
    main_window.showFullScreen()
    # Można chować przyciski, menu layout, itp.
    main_window.menu_widget.hide()

def disable_kiosk_mode(main_window):
    """
    Przywraca normalny widok.
    """
    main_window.showNormal()
    main_window.menu_widget.show()
