"""
multi_user_mode.py
Keyword: gui_data_multi_user

Obsługa wielu użytkowników, każdy ma własne ustawienia (motyw, filtry, historia).
Prosta atrapa z zapisem do słownika "user_profiles".
"""

user_profiles = {}  # np. { "alice": {"theme": "dark", "filters": [...], ...}, "bob": {...} }

def switch_user(main_window, username):
    """
    Przełącza się na profil 'username', wczytuje ustawienia.
    """
    if username not in user_profiles:
        user_profiles[username] = {"theme": "light", "filters": [], "history": []}
    profile = user_profiles[username]
    # Np. zmiana motywu
    if profile["theme"] == "dark":
        from ui.theme_handler import apply_theme
        apply_theme(main_window, "dark")
    # Inne ustawienia, np. filtry, itp.
    return profile
