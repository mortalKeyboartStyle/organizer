from ui.main_menu_folder.footer_methods import FooterMethods

class MainWindow(QMainWindow,
                 LeftMenuMethods,
                 PoczatekMethods,
                 NettoolsMethods,
                 FooterMethods):
    """
    MainWindow dziedziczy również FooterMethods, 
    więc on_prev_page_clicked, on_next_page_clicked, update_clock
    znajdują się w FooterMethods.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("infoHunter (Puzzle-Like)")
        self.setGeometry(100, 100, 1200, 700)

        # 1) Główny layout - QVBoxLayout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_vbox = QVBoxLayout(self.central_widget)

        # 2) Góra: HBox (menu + QToolBox)
        self.top_widget = QWidget()
        self.top_layout = QHBoxLayout(self.top_widget)

        self.menu_widget = QWidget()
        self.menu_layout = build_left_menu(self)
        self.menu_widget.setLayout(self.menu_layout)
        self.top_layout.addWidget(self.menu_widget, 1)

        self.main_toolbox = QToolBox()
        build_poczatek_tab(self)
        build_nettools_tab(self)
        self.top_layout.addWidget(self.main_toolbox, 3)

        self.top_widget.setLayout(self.top_layout)
        self.main_vbox.addWidget(self.top_widget)

        # 3) Stopka
        self.footer_widget = QWidget()
        self.footer_widget.setFixedHeight(50)
        self.footer_layout = QHBoxLayout(self.footer_widget)
        self.footer_layout.setContentsMargins(10, 5, 10, 5)

        self.prev_button = QPushButton("<< Poprzednia strona")
        self.prev_button.clicked.connect(self.on_prev_page_clicked) 
        self.footer_layout.addWidget(self.prev_button)

        self.next_button = QPushButton("Następna strona >>")
        self.next_button.clicked.connect(self.on_next_page_clicked)
        self.footer_layout.addWidget(self.next_button)

        self.footer_layout.addStretch()

        self.clock_label = QLabel("00:00:00")
        self.footer_layout.addWidget(self.clock_label)

        self.footer_widget.setLayout(self.footer_layout)
        self.main_vbox.addWidget(self.footer_widget)

        # 4) Dane + harmonogram
        self.results_data = []
        run_scheduler_in_background()

        # 5) Timer do zegara
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_clock)  # Odwołanie do FooterMethods.update_clock
        self.clock_timer.start(1000)
        self.update_clock()  # startowo ustawia czas
