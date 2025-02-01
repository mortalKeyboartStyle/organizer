# /home/dev/Desktop/o3organiz3r/gui/window_logic/footer/footer_methods.py

from gui.window_logic.footer.clock_logic import update_footer_clock
from gui.window_logic.footer.calendar_logic import update_footer_calendar

def init_footer_logic(footer_instance):
    """
    Inicjalizacja logiki backendu stopki – wypisuje komunikat w terminalu.
    """
    try:
        print("Footer backend logic initialized.")
    except Exception as e:
        print("Error in init_footer_logic:", e)

def update_footer_display(footer_instance):
    """
    Aktualizuje wyświetlanie zegara i daty w stopce.
    """
    try:
        update_footer_clock(footer_instance.clock_label)
        update_footer_calendar(footer_instance.date_label)
    except Exception as e:
        print("Error in update_footer_display:", e)

def open_start_menu_footer(footer_instance):
    """
    Wyświetla dynamiczne menu Start, imitujące wygląd i działanie menu w Kali Linux.
    Menu zawiera przykładowe opcje oraz placeholderowe akcje.
    """
    from PyQt6.QtWidgets import QMenu
    from PyQt6.QtGui import QCursor
    try:
        menu = QMenu()
        menu.addAction("Powiadomienia", lambda: print("[Dynamic Menu] Powiadomienia selected"))
        menu.addAction("Slack", lambda: print("[Dynamic Menu] Slack selected"))
        menu.addAction("Ustawienia", lambda: print("[Dynamic Menu] Ustawienia selected"))
        menu.addAction("O programie", lambda: print("[Dynamic Menu] O programie selected"))
        menu.addAction("Wyszukaj", lambda: print("[Dynamic Menu] Wyszukaj selected"))
        menu.addAction("Ulubione", lambda: print("[Dynamic Menu] Ulubione selected"))
        menu.addAction("Ostatnio używane", lambda: print("[Dynamic Menu] Ostatnio używane selected"))
        menu.addAction("Otwórz Terminal", lambda: print("[Dynamic Menu] Otwórz Terminal selected"))
        # Można dodać więcej opcji odpowiadających dotychczasowym usprawnieniom
        menu.exec(QCursor.pos())
    except Exception as e:
        print("Error in open_start_menu_footer:", e)

def activate_footer_menu(footer_instance):
    """
    Aktywacja dynamicznego menu stopki – najpierw wypisuje komunikat, potem otwiera menu.
    """
    init_footer_logic(footer_instance)
    open_start_menu_footer(footer_instance)
