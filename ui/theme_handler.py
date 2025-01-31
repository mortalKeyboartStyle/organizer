# theme_handler.py
# Keyword: theme_handler_basic

LIGHT_THEME = """
QWidget {
    background-color: white;
    color: black;
}
"""

DARK_THEME = """
QWidget {
    background-color: #2B2B2B;
    color: #FFFFFF;
}
"""

def apply_theme(main_window, theme="light"):
    """
    Zmienia motyw aplikacji. 'light' lub 'dark'.
    """
    if theme == "dark":
        main_window.setStyleSheet(DARK_THEME)
    else:
        main_window.setStyleSheet(LIGHT_THEME)
