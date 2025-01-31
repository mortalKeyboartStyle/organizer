from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton

def build_left_menu(main_window):
    """
    Tworzy layout (QVBoxLayout) z elementami lewego menu:
      - Pole URL
      - Przycisk Start
      - Przycisk Pokaż historię
      - Przycisk Eksportuj wyniki
      - Przycisk Filtry
      - Przycisk Zmień motyw
      - Przycisk Zaplanuj zadanie
      - Przycisk Wyczyść wyniki

    Następnie zwraca ten layout.
    'main_window' jest instancją klasy MainWindow,
    która dziedziczy również LeftMenuMethods.
    """
    menu_layout = QVBoxLayout()

    url_label = QLabel("URL (placeholder):")
    menu_layout.addWidget(url_label)

    main_window.url_input = QLineEdit()
    main_window.url_input.setPlaceholderText("np. http://example.com")
    menu_layout.addWidget(main_window.url_input)

    start_button = QPushButton("Start")
    start_button.clicked.connect(main_window.on_start_button_clicked)
    menu_layout.addWidget(start_button)

    history_button = QPushButton("Pokaż historię")
    history_button.clicked.connect(main_window.on_history_button_clicked)
    menu_layout.addWidget(history_button)

    export_button = QPushButton("Eksportuj wyniki")
    export_button.clicked.connect(main_window.on_export_button_clicked)
    menu_layout.addWidget(export_button)

    filter_button = QPushButton("Filtry (przykładowe)")
    filter_button.clicked.connect(main_window.on_filter_button_clicked)
    menu_layout.addWidget(filter_button)

    theme_button = QPushButton("Zmień motyw")
    theme_button.clicked.connect(main_window.on_theme_button_clicked)
    menu_layout.addWidget(theme_button)

    schedule_button = QPushButton("Zaplanuj zadanie (test)")
    schedule_button.clicked.connect(main_window.on_schedule_button_clicked)
    menu_layout.addWidget(schedule_button)

    clear_button = QPushButton("Wyczyść wyniki")
    clear_button.clicked.connect(main_window.on_clear_button_clicked)
    menu_layout.addWidget(clear_button)

    menu_layout.addStretch()

    return menu_layout
