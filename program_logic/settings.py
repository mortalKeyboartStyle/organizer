# Ustawienie pełnoekranowego uruchomienia aplikacji
FULL_SCREEN = True

# Definicja stylów (przykładowe style: "8bit" oraz "modern")
STYLES = {
    "8bit": """
        QMainWindow {
            background-color: #2d2d2d;
        }
        QLabel {
            color: #00ff00;
            font-family: 'Press Start 2P', cursive;
            font-size: 12px;
        }
        QPushButton {
            border: 1px solid #00ff00;
            background-color: #000;
        }
    """,
    "modern": """
        QMainWindow {
            background-color: #ffffff;
        }
        QLabel {
            color: #333333;
            font-family: Arial;
            font-size: 14px;
        }
        QPushButton {
            border: none;
            background-color: #0078d7;
            color: #ffffff;
        }
    """
}

# Wybór aktualnego stylu – zmiana np. na "modern" zmieni wygląd całej aplikacji
CURRENT_STYLE = STYLES["8bit"]

# Keywords: settings, configuration, fullscreen, styles, PyQt6
