from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget, QLabel, QLineEdit, QPushButton,
    QPlainTextEdit, QTableWidget, QTableWidgetItem
)


def build_poczatek_tab(main_window):
    """
    Tworzy widget [poczatek_page], w którym umieszczamy QTabWidget (7 wewnętrznych zakładek).
    Na końcu dołączamy go do main_window.main_toolbox jako "[poczatek]".

    'main_window' to instancja klasy MainWindow (dziedzicząca PoczatekMethods),
    więc ma dostęp do metod run_simple_fuzz, test_sentiment, itp.
    """

    # Główny widget i layout
    poczatek_page = QWidget()
    poczatek_layout = QVBoxLayout(poczatek_page)

    # Tworzymy QTabWidget i przypisujemy do main_window (jeśli chcesz mieć do niego dostęp w metodach)
    main_window.tabs = QTabWidget()

    # ---------------- Zakładka 1: Wyniki ----------------
    results_tab = QWidget()
    results_tab_layout = QVBoxLayout(results_tab)
    placeholder_results_label = QLabel("Placeholder - Wyniki")
    results_tab_layout.addWidget(placeholder_results_label)
    results_tab.setLayout(results_tab_layout)
    main_window.tabs.addTab(results_tab, "Wyniki")

    # ---------------- Zakładka 2: Statystyki ----------------
    stats_tab = QWidget()
    stats_tab_layout = QVBoxLayout(stats_tab)
    placeholder_stats_label = QLabel("Placeholder - Statystyki")
    stats_tab_layout.addWidget(placeholder_stats_label)
    stats_tab.setLayout(stats_tab_layout)
    main_window.tabs.addTab(stats_tab, "Statystyki")

    # ---------------- Zakładka 3: FuzzScrap ----------------
    fuzzscrap_tab = QWidget()
    fuzzscrap_layout = QVBoxLayout(fuzzscrap_tab)

    fuzz_url_label = QLabel("URL do fuzzingu:")
    fuzzscrap_layout.addWidget(fuzz_url_label)
    main_window.fuzz_url_input = QLineEdit("http://example.com/search")
    fuzzscrap_layout.addWidget(main_window.fuzz_url_input)

    fuzz_param_label = QLabel("Nazwa parametru GET (np. search):")
    fuzzscrap_layout.addWidget(fuzz_param_label)
    main_window.fuzz_param_input = QLineEdit("search")
    fuzzscrap_layout.addWidget(main_window.fuzz_param_input)

    fuzz_words_label = QLabel("Słowa do fuzzingu (rozdzielone przecinkami):")
    fuzzscrap_layout.addWidget(fuzz_words_label)
    main_window.fuzz_words_input = QLineEdit("promo,discount,secret,admin")
    fuzzscrap_layout.addWidget(main_window.fuzz_words_input)

    fuzz_button = QPushButton("Uruchom Fuzz parametru GET")
    fuzz_button.clicked.connect(main_window.run_simple_fuzz)  # Metoda w PoczatekMethods
    fuzzscrap_layout.addWidget(fuzz_button)

    dir_url_label = QLabel("URL do bruteforce ścieżek:")
    fuzzscrap_layout.addWidget(dir_url_label)
    main_window.dir_url_input = QLineEdit("http://example.com")
    fuzzscrap_layout.addWidget(main_window.dir_url_input)

    dir_wordlist_label = QLabel("Wordlist (rozdzielone przecinkami):")
    fuzzscrap_layout.addWidget(dir_wordlist_label)
    main_window.dir_wordlist_input = QLineEdit("admin,login,secret,images")
    fuzzscrap_layout.addWidget(main_window.dir_wordlist_input)

    dir_button = QPushButton("Bruteforce ścieżek")
    dir_button.clicked.connect(main_window.run_directory_bruteforce)
    fuzzscrap_layout.addWidget(dir_button)

    main_window.fuzz_results_table = QTableWidget()
    main_window.fuzz_results_table.setColumnCount(3)
    main_window.fuzz_results_table.setHorizontalHeaderLabels(["URL", "Status", "Sample/Error"])
    fuzzscrap_layout.addWidget(main_window.fuzz_results_table)

    fuzzscrap_tab.setLayout(fuzzscrap_layout)
    main_window.tabs.addTab(fuzzscrap_tab, "FuzzScrap")

    # ---------------- Zakładka 4: AI/Analysis ----------------
    ai_tab = QWidget()
    ai_layout = QVBoxLayout(ai_tab)

    ai_link_label = QLabel("Link do analizy AI:")
    ai_layout.addWidget(ai_link_label)
    main_window.ai_link_input = QLineEdit("http://example.com/promo")
    ai_layout.addWidget(main_window.ai_link_input)

    ai_sentiment_btn = QPushButton("Analiza Sentiment")
    ai_sentiment_btn.clicked.connect(main_window.test_sentiment)
    ai_layout.addWidget(ai_sentiment_btn)

    ai_classify_btn = QPushButton("Klasyfikacja Linku (promocyjny?)")
    ai_classify_btn.clicked.connect(main_window.test_link_classify)
    ai_layout.addWidget(ai_classify_btn)

    ai_summary_btn = QPushButton("Streszczenie przykładowego tekstu")
    ai_summary_btn.clicked.connect(main_window.test_summary)
    ai_layout.addWidget(ai_summary_btn)

    ai_forum_btn = QPushButton("Analiza forów (top słowa)")
    ai_forum_btn.clicked.connect(main_window.test_forum_analyze)
    ai_layout.addWidget(ai_forum_btn)

    ai_reco_btn = QPushButton("System rekomendacji (prosty)")
    ai_reco_btn.clicked.connect(main_window.test_recommendations)
    ai_layout.addWidget(ai_reco_btn)

    ai_spam_btn = QPushButton("Wykryj spam / phishing")
    ai_spam_btn.clicked.connect(main_window.test_spam_detect)
    ai_layout.addWidget(ai_spam_btn)

    ai_topic_btn = QPushButton("Wykryj kategorię (Topic Modelling)")
    ai_topic_btn.clicked.connect(main_window.test_topic_modelling)
    ai_layout.addWidget(ai_topic_btn)

    ai_social_btn = QPushButton("Analiza social (mock Twitter)")
    ai_social_btn.clicked.connect(main_window.test_social_sentiment)
    ai_layout.addWidget(ai_social_btn)

    ai_popularity_btn = QPushButton("Popularność linku (mock)")
    ai_popularity_btn.clicked.connect(main_window.test_popularity)
    ai_layout.addWidget(ai_popularity_btn)

    ai_image_btn = QPushButton("Atrapa OCR - image_ai_handler")
    ai_image_btn.clicked.connect(main_window.test_fake_ocr)
    ai_layout.addWidget(ai_image_btn)

    main_window.ai_results_box = QPlainTextEdit()
    ai_layout.addWidget(main_window.ai_results_box)

    ai_tab.setLayout(ai_layout)
    main_window.tabs.addTab(ai_tab, "AI/Analysis")

    # ---------------- Zakładka 5: GUI/Data ----------------
    gdata_tab = QWidget()
    gdata_layout = QVBoxLayout(gdata_tab)

    dashboard_btn = QPushButton("Pokaż 'dashboard' domen")
    dashboard_btn.clicked.connect(main_window.show_dashboard_example)
    gdata_layout.addWidget(dashboard_btn)

    kiosk_btn = QPushButton("Włącz tryb kiosk")
    kiosk_btn.clicked.connect(lambda: main_window.enable_kiosk_mode(main_window))
    gdata_layout.addWidget(kiosk_btn)

    kiosk_off_btn = QPushButton("Wyłącz tryb kiosk")
    kiosk_off_btn.clicked.connect(lambda: main_window.disable_kiosk_mode(main_window))
    gdata_layout.addWidget(kiosk_off_btn)

    tabs_btn = QPushButton("Dodaj nową zakładkę 'Nowa'")
    tabs_btn.clicked.connect(lambda: main_window.add_new_tab(main_window, "Nowa"))
    gdata_layout.addWidget(tabs_btn)

    columns_add_btn = QPushButton("Dodaj kolumnę 'Ocena'")
    columns_add_btn.clicked.connect(lambda: main_window.add_custom_column(main_window, "Ocena"))
    gdata_layout.addWidget(columns_add_btn)

    columns_del_btn = QPushButton("Usuń ostatnią kolumnę")
    columns_del_btn.clicked.connect(main_window.remove_last_column)
    gdata_layout.addWidget(columns_del_btn)

    users_btn = QPushButton("Przełącz użytkownika 'Alice'")
    users_btn.clicked.connect(lambda: main_window.switch_user(main_window, "alice"))
    gdata_layout.addWidget(users_btn)

    dragdrop_btn = QPushButton("Włącz drag&drop w tabeli głównej")
    dragdrop_btn.clicked.connect(main_window.enable_dragdrop_main_table)
    gdata_layout.addWidget(dragdrop_btn)

    editable_btn = QPushButton("Uczyń tabelę główną edytowalną")
    editable_btn.clicked.connect(main_window.make_main_table_editable)
    gdata_layout.addWidget(editable_btn)

    tray_btn = QPushButton("Minimalizuj do traya (ikona test.png)")
    tray_btn.clicked.connect(lambda: main_window.enable_system_tray(main_window, "test.png"))
    gdata_layout.addWidget(tray_btn)

    main_window.timeline_data = []
    timeline_btn = QPushButton("Dodaj link do timeline + pokaż")
    timeline_btn.clicked.connect(main_window.test_timeline)
    gdata_layout.addWidget(timeline_btn)

    config_btn = QPushButton("Wczytaj/Zapisz config (theme=dark)")
    config_btn.clicked.connect(main_window.test_config_save_load)
    gdata_layout.addWidget(config_btn)

    main_window.gdata_output = QPlainTextEdit()
    gdata_layout.addWidget(main_window.gdata_output)
    gdata_tab.setLayout(gdata_layout)
    main_window.tabs.addTab(gdata_tab, "GUI/Data")

    # ---------------- Zakładka 6: Net/API ----------------
    netapi_tab = QWidget()
    netapi_layout = QVBoxLayout(netapi_tab)

    db_init_btn = QPushButton("Inicjalizuj DB (SQLite)")
    db_init_btn.clicked.connect(main_window.test_db_init)
    netapi_layout.addWidget(db_init_btn)

    db_save_btn = QPushButton("Zapisz URL do DB")
    db_save_btn.clicked.connect(main_window.test_db_save)
    netapi_layout.addWidget(db_save_btn)

    db_load_btn = QPushButton("Odczytaj historię z DB")
    db_load_btn.clicked.connect(main_window.test_db_load)
    netapi_layout.addWidget(db_load_btn)

    rest_btn = QPushButton("Uruchom prosty REST (Flask, port=5000)")
    rest_btn.clicked.connect(lambda: main_window.run_rest_api())
    netapi_layout.addWidget(rest_btn)

    email_btn = QPushButton("Wyślij testowego maila (mock)")
    email_btn.clicked.connect(main_window.test_email_send)
    netapi_layout.addWidget(email_btn)

    chat_btn = QPushButton("Slack/Telegram - test")
    chat_btn.clicked.connect(main_window.test_chat_send)
    netapi_layout.addWidget(chat_btn)

    plugin_btn = QPushButton("Załaduj pluginy z plugins/")
    plugin_btn.clicked.connect(main_window.test_plugin_manager)
    netapi_layout.addWidget(plugin_btn)

    graphql_btn = QPushButton("Test GraphQL zapytania")
    graphql_btn.clicked.connect(main_window.test_graphql)
    netapi_layout.addWidget(graphql_btn)

    geo_btn = QPushButton("Geokoduj 'Warsaw'")
    geo_btn.clicked.connect(main_window.test_geocode)
    netapi_layout.addWidget(geo_btn)

    docker_btn = QPushButton("Stwórz Dockerfile")
    docker_btn.clicked.connect(main_window.test_dockerfile)
    netapi_layout.addWidget(docker_btn)

    server_btn = QPushButton("Uruchom tryb server (Flask port=8080)")
    server_btn.clicked.connect(lambda: main_window.run_server_mode())
    netapi_layout.addWidget(server_btn)

    enc_btn = QPushButton("Szyfruj/Deszyfruj 'sekret'")
    enc_btn.clicked.connect(main_window.test_encrypt)
    netapi_layout.addWidget(enc_btn)

    main_window.netapi_output = QPlainTextEdit()
    netapi_layout.addWidget(main_window.netapi_output)
    netapi_tab.setLayout(netapi_layout)
    main_window.tabs.addTab(netapi_tab, "Net/API")

    # ---------------- Zakładka 7: Sec/Automation ----------------
    secauto_tab = QWidget()
    secauto_layout = QVBoxLayout(secauto_tab)

    encrypt_btn = QPushButton("Zaszyfruj 'hello' i odszyfruj")
    encrypt_btn.clicked.connect(main_window.test_encrypt_decrypt)
    secauto_layout.addWidget(encrypt_btn)

    tests_btn = QPushButton("Uruchom testy (sample_test)")
    tests_btn.clicked.connect(main_window.test_run_tests)
    secauto_layout.addWidget(tests_btn)

    secscan_btn = QPushButton("Skan bezpieczeństwa: 'http://example.com/<script>'")
    secscan_btn.clicked.connect(main_window.test_security_scan)
    secauto_layout.addWidget(secscan_btn)

    audit_btn = QPushButton("Filtruj logi 'ERROR' w debug.log")
    audit_btn.clicked.connect(main_window.test_audit_logs)
    secauto_layout.addWidget(audit_btn)

    migrations_btn = QPushButton("Uruchom migracje DB (migrations_handler)")
    migrations_btn.clicked.connect(main_window.test_migrations)
    secauto_layout.addWidget(migrations_btn)

    cicd_btn = QPushButton("Uruchom pipeline (pytest + flake8)")
    cicd_btn.clicked.connect(main_window.test_ci_cd)
    secauto_layout.addWidget(cicd_btn)

    profile_btn = QPushButton("Profiluj prostą funkcję scrapowania")
    profile_btn.clicked.connect(main_window.test_profiling)
    secauto_layout.addWidget(profile_btn)

    fuzzplugin_btn = QPushButton("Wczytaj słowa z 'fuzz_dictionary.txt'")
    fuzzplugin_btn.clicked.connect(main_window.test_fuzz_plugins)
    secauto_layout.addWidget(fuzzplugin_btn)

    cli_btn = QPushButton("Wypisz przykładowe argumenty CLI")
    cli_btn.clicked.connect(main_window.test_cli_mode)
    secauto_layout.addWidget(cli_btn)

    duplicates_btn = QPushButton("Sprawdź duplikat linku 'http://example.com'")
    duplicates_btn.clicked.connect(main_window.test_duplicates)
    secauto_layout.addWidget(duplicates_btn)

    main_window.secauto_output = QPlainTextEdit()
    secauto_layout.addWidget(main_window.secauto_output)
    secauto_tab.setLayout(secauto_layout)
    main_window.tabs.addTab(secauto_tab, "Sec/Automation")

    # Dodajemy QTabWidget do layoutu i do main_window.main_toolbox
    poczatek_layout.addWidget(main_window.tabs)
    poczatek_page.setLayout(poczatek_layout)

    # Ostatecznie dołączamy powstały widget do main_window.main_toolbox
    main_window.main_toolbox.addItem(poczatek_page, "[poczatek]")
