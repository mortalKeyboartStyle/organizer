# notification_handler.py
# Keyword: notification_handler_basic

import platform

def send_notification(title, message):
    """
    Wysyła powiadomienie systemowe, zależnie od OS.
    """
    os_name = platform.system().lower()
    if "linux" in os_name:
        try:
            import notify2
            notify2.init("WyszukiwaczPromocji")
            n = notify2.Notification(title, message)
            n.show()
        except ImportError:
            print("notify2 nie jest zainstalowany.")
    elif "windows" in os_name:
        # Można użyć win10toast lub innej biblioteki
        print("Powiadomienie Windows: ", title, message)
    else:
        print(f"Powiadomienie {os_name}: {title}, {message}")
