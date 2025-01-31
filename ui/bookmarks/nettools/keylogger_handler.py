# ui/bookmarks/nettools/keylogger_handler.py
try:
    from pynput import keyboard
except ImportError:
    keyboard = None

def start_keylogger_mock():
    """
    Atrapa keyloggera, demonstruje idea.
    W realnym - listener OnPress, OnRelease + zapis do pliku.
    """
    if not keyboard:
        return "[Keylogger] Brak biblioteki pynput. Zainstaluj: pip install pynput"

    # Minimalny mock
    return "[Keylogger] Start keylogger mock. W realnej wersji -> keyboard.Listener(...)"
