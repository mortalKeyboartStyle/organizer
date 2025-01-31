import re
import logging
import sys

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel,
    QTableWidget, QTableWidgetItem, QMessageBox, QTabWidget, QFileDialog, QPlainTextEdit,
    QApplication, QToolBox
)

# --- Importy istniejących modułów do scrapingu/filtrów/historii itd. ---
from ui.scraping_handler import start_scraping
from ui.history_handler import save_to_history, load_history
from ui.export_handler import export_to_csv
from ui.stats_handler import generate_statistics
from ui.filter_handler import filter_results
from ui.tag_selector import get_user_tags
from ui.scheduler_handler import schedule_job, run_scheduler_in_background
from ui.theme_handler import apply_theme
from ui.notification_handler import send_notification

# --- FuzzScrap ---
from ui.bookmarks.fuzzscrap.web_fuzzing_handler import simple_get_fuzz
from ui.bookmarks.fuzzscrap.extended_fuzz_handler import directory_bruteforce

# --- AI/Analysis ---
from ui.bookmarks.ai_analysis.sentiment_handler import simple_sentiment_analysis
from ui.bookmarks.ai_analysis.link_classifier import classify_link
from ui.bookmarks.ai_analysis.summaries_handler import simple_summary
from ui.bookmarks.ai_analysis.forum_handler import analyze_forum_threads
from ui.bookmarks.ai_analysis.recommendation_handler import recommend_links
from ui.bookmarks.ai_analysis.image_ai_handler import fake_ocr
from ui.bookmarks.ai_analysis.spam_detector import detect_spam_phishing
from ui.bookmarks.ai_analysis.topic_modelling import simple_topic_detect
from ui.bookmarks.ai_analysis.social_sentiment import mock_twitter_sentiment
from ui.bookmarks.ai_analysis.links_popularity import check_popularity

# --- GUI/Data ---
from ui.bookmarks.gui_data.dashboard_handler import get_chart_data, generate_pie_data
from ui.bookmarks.gui_data.kiosk_mode import enable_kiosk_mode, disable_kiosk_mode
from ui.bookmarks.gui_data.tabs_handler import add_new_tab
from ui.bookmarks.gui_data.columns_config import add_custom_column, remove_custom_column
from ui.bookmarks.gui_data.multi_user_mode import switch_user
from ui.bookmarks.gui_data.dragdrop_handler import enable_drag_drop_for_table
from ui.bookmarks.gui_data.editable_table import make_table_editable
from ui.bookmarks.gui_data.tray_handler import enable_system_tray
from ui.bookmarks.gui_data.timeline_handler import add_link_to_timeline, get_timeline_display
from ui.bookmarks.gui_data.config_manager import load_config, save_config, get_theme, set_theme

# --- Net/API ---
from ui.bookmarks.net_api.db_handler import init_db, save_link_to_db, load_history_from_db
from ui.bookmarks.net_api.rest_handler import run_rest_api
from ui.bookmarks.net_api.email_handler import send_email_with_attachment
from ui.bookmarks.net_api.chat_handler import send_slack_message, send_telegram_message
from ui.bookmarks.net_api.plugin_manager import load_plugins
from ui.bookmarks.net_api.graphql_handler import execute_graphql
from ui.bookmarks.net_api.geoapi_handler import geocode_address
from ui.bookmarks.net_api.docker_handler import create_dockerfile
from ui.bookmarks.net_api.server_mode import run_server_mode
from ui.bookmarks.net_api.encrypt_handler import encrypt_data as net_encrypt_data, decrypt_data as net_decrypt_data

# --- Sec/Automation ---
from ui.bookmarks.sec_automation.encrypt_handler import encrypt_data, decrypt_data
from ui.bookmarks.sec_automation.test_handler import run_basic_tests
from ui.bookmarks.sec_automation.security_scan import simple_security_scan
from ui.bookmarks.sec_automation.audit_log_handler import filter_logs
from ui.bookmarks.sec_automation.migrations_handler import run_migration
from ui.bookmarks.sec_automation.ci_cd_handler import run_ci_pipeline
from ui.bookmarks.sec_automation.profiling_handler import profile_function
from ui.bookmarks.sec_automation.fuzz_plugins import load_fuzz_dictionary
from ui.bookmarks.sec_automation.cli_mode import parse_cli_args
from ui.bookmarks.sec_automation.duplicate_detector import check_duplicates


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("infoHunter")
        self.setGeometry(100, 100, 1200, 700)

        # ------------------ Główny widget i layout poziomy ------------------
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)

        # ------------------ LEWA STRONA (menu) - BEZ ZMIAN ------------------
        self.menu_widget = QWidget()
        self.menu_layout = QVBoxLayout(self.menu_widget)

        self.url_label = QLabel("URL (placeholder):")
        self.menu_layout.addWidget(self.url_label)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("np. http://example.com")
        self.menu_layout.addWidget(self.url_input)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.on_start_button_clicked)
        self.menu_layout.addWidget(self.start_button)

        self.history_button = QPushButton("Pokaż historię")
        self.history_button.clicked.connect(self.on_history_button_clicked)
        self.menu_layout.addWidget(self.history_button)

        self.export_button = QPushButton("Eksportuj wyniki")
        self.export_button.clicked.connect(self.on_export_button_clicked)
        self.menu_layout.addWidget(self.export_button)

        self.filter_button = QPushButton("Filtry (przykładowe)")
        self.filter_button.clicked.connect(self.on_filter_button_clicked)
        self.menu_layout.addWidget(self.filter_button)

        self.theme_button = QPushButton("Zmień motyw")
        self.theme_button.clicked.connect(self.on_theme_button_clicked)
        self.menu_layout.addWidget(self.theme_button)

        self.schedule_button = QPushButton("Zaplanuj zadanie (test)")
        self.schedule_button.clicked.connect(self.on_schedule_button_clicked)
        self.menu_layout.addWidget(self.schedule_button)

        self.clear_button = QPushButton("Wyczyść wyniki")
        self.clear_button.clicked.connect(self.on_clear_button_clicked)
        self.menu_layout.addWidget(self.clear_button)

        self.menu_layout.addStretch()
        self.menu_widget.setLayout(self.menu_layout)

        # ------------------ PRAWA STRONA: QToolBox z dwiema sekcjami ------------------
        self.main_toolbox = QToolBox()

        # (1) Strona [poczatek] - zawiera QTabWidget z dawnych 7 zakładek
        self.poczatek_page = QWidget()
        self.poczatek_layout = QVBoxLayout(self.poczatek_page)

        self.tabs = QTabWidget()

        # --- Zakładka 1: Wyniki (placeholder)
        self.results_tab = QWidget()
        self.results_tab_layout = QVBoxLayout(self.results_tab)
        self.placeholder_results_label = QLabel("Placeholder - Wyniki")
        self.results_tab_layout.addWidget(self.placeholder_results_label)
        self.results_tab.setLayout(self.results_tab_layout)
        self.tabs.addTab(self.results_tab, "Wyniki")

        # --- Zakładka 2: Statystyki (placeholder)
        self.stats_tab = QWidget()
        self.stats_tab_layout = QVBoxLayout(self.stats_tab)
        self.placeholder_stats_label = QLabel("Placeholder - Statystyki")
        self.stats_tab_layout.addWidget(self.placeholder_stats_label)
        self.stats_tab.setLayout(self.stats_tab_layout)
        self.tabs.addTab(self.stats_tab, "Statystyki")

        # (3) FuzzScrap
        self.fuzzscrap_tab = QWidget()
        self.fuzzscrap_layout = QVBoxLayout(self.fuzzscrap_tab)

        self.fuzz_url_label = QLabel("URL do fuzzingu:")
        self.fuzzscrap_layout.addWidget(self.fuzz_url_label)
        self.fuzz_url_input = QLineEdit("http://example.com/search")
        self.fuzzscrap_layout.addWidget(self.fuzz_url_input)

        self.fuzz_param_label = QLabel("Nazwa parametru GET (np. search):")
        self.fuzzscrap_layout.addWidget(self.fuzz_param_label)
        self.fuzz_param_input = QLineEdit("search")
        self.fuzzscrap_layout.addWidget(self.fuzz_param_input)

        self.fuzz_words_label = QLabel("Słowa do fuzzingu (rozdzielone przecinkami):")
        self.fuzzscrap_layout.addWidget(self.fuzz_words_label)
        self.fuzz_words_input = QLineEdit("promo,discount,secret,admin")
        self.fuzzscrap_layout.addWidget(self.fuzz_words_input)

        self.fuzz_button = QPushButton("Uruchom Fuzz parametru GET")
        self.fuzz_button.clicked.connect(self.run_simple_fuzz)
        self.fuzzscrap_layout.addWidget(self.fuzz_button)

        self.dir_url_label = QLabel("URL do bruteforce ścieżek:")
        self.fuzzscrap_layout.addWidget(self.dir_url_label)
        self.dir_url_input = QLineEdit("http://example.com")
        self.fuzzscrap_layout.addWidget(self.dir_url_input)

        self.dir_wordlist_label = QLabel("Wordlist (rozdzielone przecinkami):")
        self.fuzzscrap_layout.addWidget(self.dir_wordlist_label)
        self.dir_wordlist_input = QLineEdit("admin,login,secret,images")
        self.fuzzscrap_layout.addWidget(self.dir_wordlist_input)

        self.dir_button = QPushButton("Bruteforce ścieżek")
        self.dir_button.clicked.connect(self.run_directory_bruteforce)
        self.fuzzscrap_layout.addWidget(self.dir_button)

        self.fuzz_results_table = QTableWidget()
        self.fuzz_results_table.setColumnCount(3)
        self.fuzz_results_table.setHorizontalHeaderLabels(["URL", "Status", "Sample/Error"])
        self.fuzzscrap_layout.addWidget(self.fuzz_results_table)

        self.fuzzscrap_tab.setLayout(self.fuzzscrap_layout)
        self.tabs.addTab(self.fuzzscrap_tab, "FuzzScrap")

        # (4) AI/Analysis
        self.ai_tab = QWidget()
        self.ai_layout = QVBoxLayout(self.ai_tab)

        self.ai_link_label = QLabel("Link do analizy AI:")
        self.ai_layout.addWidget(self.ai_link_label)
        self.ai_link_input = QLineEdit("http://example.com/promo")
        self.ai_layout.addWidget(self.ai_link_input)

        self.ai_sentiment_btn = QPushButton("Analiza Sentiment")
        self.ai_sentiment_btn.clicked.connect(self.test_sentiment)
        self.ai_layout.addWidget(self.ai_sentiment_btn)

        self.ai_classify_btn = QPushButton("Klasyfikacja Linku (promocyjny?)")
        self.ai_classify_btn.clicked.connect(self.test_link_classify)
        self.ai_layout.addWidget(self.ai_classify_btn)

        self.ai_summary_btn = QPushButton("Streszczenie przykładowego tekstu")
        self.ai_summary_btn.clicked.connect(self.test_summary)
        self.ai_layout.addWidget(self.ai_summary_btn)

        self.ai_forum_btn = QPushButton("Analiza forów (top słowa)")
        self.ai_forum_btn.clicked.connect(self.test_forum_analyze)
        self.ai_layout.addWidget(self.ai_forum_btn)

        self.ai_reco_btn = QPushButton("System rekomendacji (prosty)")
        self.ai_reco_btn.clicked.connect(self.test_recommendations)
        self.ai_layout.addWidget(self.ai_reco_btn)

        self.ai_spam_btn = QPushButton("Wykryj spam / phishing")
        self.ai_spam_btn.clicked.connect(self.test_spam_detect)
        self.ai_layout.addWidget(self.ai_spam_btn)

        self.ai_topic_btn = QPushButton("Wykryj kategorię (Topic Modelling)")
        self.ai_topic_btn.clicked.connect(self.test_topic_modelling)
        self.ai_layout.addWidget(self.ai_topic_btn)

        self.ai_social_btn = QPushButton("Analiza social (mock Twitter)")
        self.ai_social_btn.clicked.connect(self.test_social_sentiment)
        self.ai_layout.addWidget(self.ai_social_btn)

        self.ai_popularity_btn = QPushButton("Popularność linku (mock)")
        self.ai_popularity_btn.clicked.connect(self.test_popularity)
        self.ai_layout.addWidget(self.ai_popularity_btn)

        self.ai_image_btn = QPushButton("Atrapa OCR - image_ai_handler")
        self.ai_image_btn.clicked.connect(self.test_fake_ocr)
        self.ai_layout.addWidget(self.ai_image_btn)

        self.ai_results_box = QPlainTextEdit()
        self.ai_layout.addWidget(self.ai_results_box)
        self.ai_tab.setLayout(self.ai_layout)
        self.tabs.addTab(self.ai_tab, "AI/Analysis")

        # (5) GUI/Data
        self.gdata_tab = QWidget()
        self.gdata_layout = QVBoxLayout(self.gdata_tab)

        self.dashboard_btn = QPushButton("Pokaż 'dashboard' domen")
        self.dashboard_btn.clicked.connect(self.show_dashboard_example)
        self.gdata_layout.addWidget(self.dashboard_btn)

        self.kiosk_btn = QPushButton("Włącz tryb kiosk")
        self.kiosk_btn.clicked.connect(lambda: enable_kiosk_mode(self))
        self.gdata_layout.addWidget(self.kiosk_btn)

        self.kiosk_off_btn = QPushButton("Wyłącz tryb kiosk")
        self.kiosk_off_btn.clicked.connect(lambda: disable_kiosk_mode(self))
        self.gdata_layout.addWidget(self.kiosk_off_btn)

        self.tabs_btn = QPushButton("Dodaj nową zakładkę 'Nowa'")
        self.tabs_btn.clicked.connect(lambda: add_new_tab(self, "Nowa"))
        self.gdata_layout.addWidget(self.tabs_btn)

        self.columns_add_btn = QPushButton("Dodaj kolumnę 'Ocena'")
        self.columns_add_btn.clicked.connect(lambda: add_custom_column(self, "Ocena"))
        self.gdata_layout.addWidget(self.columns_add_btn)

        self.columns_del_btn = QPushButton("Usuń ostatnią kolumnę")
        self.columns_del_btn.clicked.connect(self.remove_last_column)
        self.gdata_layout.addWidget(self.columns_del_btn)

        self.users_btn = QPushButton("Przełącz użytkownika 'Alice'")
        self.users_btn.clicked.connect(lambda: switch_user(self, "alice"))
        self.gdata_layout.addWidget(self.users_btn)

        self.dragdrop_btn = QPushButton("Włącz drag&drop w tabeli głównej")
        self.dragdrop_btn.clicked.connect(self.enable_dragdrop_main_table)
        self.gdata_layout.addWidget(self.dragdrop_btn)

        self.editable_btn = QPushButton("Uczyń tabelę główną edytowalną")
        self.editable_btn.clicked.connect(self.make_main_table_editable)
        self.gdata_layout.addWidget(self.editable_btn)

        self.tray_btn = QPushButton("Minimalizuj do traya (ikona test.png)")
        self.tray_btn.clicked.connect(lambda: enable_system_tray(self, "test.png"))
        self.gdata_layout.addWidget(self.tray_btn)

        self.timeline_data = []
        self.timeline_btn = QPushButton("Dodaj link do timeline + pokaż")
        self.timeline_btn.clicked.connect(self.test_timeline)
        self.gdata_layout.addWidget(self.timeline_btn)

        self.config_btn = QPushButton("Wczytaj/Zapisz config (theme=dark)")
        self.config_btn.clicked.connect(self.test_config_save_load)
        self.gdata_layout.addWidget(self.config_btn)

        self.gdata_output = QPlainTextEdit()
        self.gdata_layout.addWidget(self.gdata_output)

        self.gdata_tab.setLayout(self.gdata_layout)
        self.tabs.addTab(self.gdata_tab, "GUI/Data")

        # (6) Net/API
        self.netapi_tab = QWidget()
        self.netapi_layout = QVBoxLayout(self.netapi_tab)

        self.db_init_btn = QPushButton("Inicjalizuj DB (SQLite)")
        self.db_init_btn.clicked.connect(self.test_db_init)
        self.netapi_layout.addWidget(self.db_init_btn)

        self.db_save_btn = QPushButton("Zapisz URL do DB")
        self.db_save_btn.clicked.connect(self.test_db_save)
        self.netapi_layout.addWidget(self.db_save_btn)

        self.db_load_btn = QPushButton("Odczytaj historię z DB")
        self.db_load_btn.clicked.connect(self.test_db_load)
        self.netapi_layout.addWidget(self.db_load_btn)

        self.rest_btn = QPushButton("Uruchom prosty REST (Flask, port=5000)")
        self.rest_btn.clicked.connect(lambda: run_rest_api())
        self.netapi_layout.addWidget(self.rest_btn)

        self.email_btn = QPushButton("Wyślij testowego maila (mock)")
        self.email_btn.clicked.connect(self.test_email_send)
        self.netapi_layout.addWidget(self.email_btn)

        self.chat_btn = QPushButton("Slack/Telegram - test")
        self.chat_btn.clicked.connect(self.test_chat_send)
        self.netapi_layout.addWidget(self.chat_btn)

        self.plugin_btn = QPushButton("Załaduj pluginy z plugins/")
        self.plugin_btn.clicked.connect(self.test_plugin_manager)
        self.netapi_layout.addWidget(self.plugin_btn)

        self.graphql_btn = QPushButton("Test GraphQL zapytania")
        self.graphql_btn.clicked.connect(self.test_graphql)
        self.netapi_layout.addWidget(self.graphql_btn)

        self.geo_btn = QPushButton("Geokoduj 'Warsaw'")
        self.geo_btn.clicked.connect(self.test_geocode)
        self.netapi_layout.addWidget(self.geo_btn)

        self.docker_btn = QPushButton("Stwórz Dockerfile")
        self.docker_btn.clicked.connect(self.test_dockerfile)
        self.netapi_layout.addWidget(self.docker_btn)

        self.server_btn = QPushButton("Uruchom tryb server (Flask port=8080)")
        self.server_btn.clicked.connect(lambda: run_server_mode())
        self.netapi_layout.addWidget(self.server_btn)

        self.enc_btn = QPushButton("Szyfruj/Deszyfruj 'sekret'")
        self.enc_btn.clicked.connect(self.test_encrypt)
        self.netapi_layout.addWidget(self.enc_btn)

        self.netapi_output = QPlainTextEdit()
        self.netapi_layout.addWidget(self.netapi_output)
        self.netapi_tab.setLayout(self.netapi_layout)
        self.tabs.addTab(self.netapi_tab, "Net/API")

        # (7) Sec/Automation
        self.secauto_tab = QWidget()
        self.secauto_layout = QVBoxLayout(self.secauto_tab)

        self.encrypt_btn = QPushButton("Zaszyfruj 'hello' i odszyfruj")
        self.encrypt_btn.clicked.connect(self.test_encrypt_decrypt)
        self.secauto_layout.addWidget(self.encrypt_btn)

        self.tests_btn = QPushButton("Uruchom testy (sample_test)")
        self.tests_btn.clicked.connect(self.test_run_tests)
        self.secauto_layout.addWidget(self.tests_btn)

        self.secscan_btn = QPushButton("Skan bezpieczeństwa: 'http://example.com/<script>'")
        self.secscan_btn.clicked.connect(self.test_security_scan)
        self.secauto_layout.addWidget(self.secscan_btn)

        self.audit_btn = QPushButton("Filtruj logi 'ERROR' w debug.log")
        self.audit_btn.clicked.connect(self.test_audit_logs)
        self.secauto_layout.addWidget(self.audit_btn)

        self.migrations_btn = QPushButton("Uruchom migracje DB (migrations_handler)")
        self.migrations_btn.clicked.connect(self.test_migrations)
        self.secauto_layout.addWidget(self.migrations_btn)

        self.cicd_btn = QPushButton("Uruchom pipeline (pytest + flake8)")
        self.cicd_btn.clicked.connect(self.test_ci_cd)
        self.secauto_layout.addWidget(self.cicd_btn)

        self.profile_btn = QPushButton("Profiluj prostą funkcję scrapowania")
        self.profile_btn.clicked.connect(self.test_profiling)
        self.secauto_layout.addWidget(self.profile_btn)

        self.fuzzplugin_btn = QPushButton("Wczytaj słowa z 'fuzz_dictionary.txt'")
        self.fuzzplugin_btn.clicked.connect(self.test_fuzz_plugins)
        self.secauto_layout.addWidget(self.fuzzplugin_btn)

        self.cli_btn = QPushButton("Wypisz przykładowe argumenty CLI")
        self.cli_btn.clicked.connect(self.test_cli_mode)
        self.secauto_layout.addWidget(self.cli_btn)

        self.duplicates_btn = QPushButton("Sprawdź duplikat linku 'http://example.com'")
        self.duplicates_btn.clicked.connect(self.test_duplicates)
        self.secauto_layout.addWidget(self.duplicates_btn)

        self.secauto_output = QPlainTextEdit()
        self.secauto_layout.addWidget(self.secauto_output)
        self.secauto_tab.setLayout(self.secauto_layout)
        self.tabs.addTab(self.secauto_tab, "Sec/Automation")

        # Dodaj QTabWidget do [poczatek]
        self.poczatek_layout.addWidget(self.tabs)
        self.poczatek_page.setLayout(self.poczatek_layout)
        self.main_toolbox.addItem(self.poczatek_page, "[poczatek]")

        # (2) Strona [nettools] - dynamiczne menu z 7 placeholderów
        self.nettools_page = QWidget()
        self.nettools_layout = QVBoxLayout(self.nettools_page)

        # Tworzymy QToolBox wewnątrz [nettools] do 7 pomysłów
        self.nettools_toolbox = QToolBox()
        self.nettools_layout.addWidget(self.nettools_toolbox)

        # 1) Skrypt do firewall
        self.firewall_widget = QWidget()
        fw_layout = QVBoxLayout(self.firewall_widget)

        fw_placeholder_btn = QPushButton("Pokaż reguły Firewall")
        fw_placeholder_btn.clicked.connect(self.run_firewall_demo)
        fw_layout.addWidget(fw_placeholder_btn)

        block_ip_btn = QPushButton("Blokuj IP 8.8.8.8")
        block_ip_btn.clicked.connect(lambda: self.run_block_ip("8.8.8.8"))
        fw_layout.addWidget(block_ip_btn)

        self.firewall_widget.setLayout(fw_layout)
        self.nettools_toolbox.addItem(self.firewall_widget, "Skrypt do firewall")

        # 2) Prosty IDS
        self.ids_widget = QWidget()
        ids_layout = QVBoxLayout(self.ids_widget)
        ids_placeholder_btn = QPushButton("Placeholder - Prosty IDS")
        ids_layout.addWidget(ids_placeholder_btn)
        self.ids_widget.setLayout(ids_layout)
        self.nettools_toolbox.addItem(self.ids_widget, "Prosty IDS")

        # 3) Code security scanner
        self.codesec_widget = QWidget()
        codesec_layout = QVBoxLayout(self.codesec_widget)
        codesec_placeholder_btn = QPushButton("Placeholder - Code security scanner")
        codesec_layout.addWidget(codesec_placeholder_btn)
        self.codesec_widget.setLayout(codesec_layout)
        self.nettools_toolbox.addItem(self.codesec_widget, "Code security scanner")

        # 4) GPU cracking panel
        self.gpucrack_widget = QWidget()
        gpu_layout = QVBoxLayout(self.gpucrack_widget)
        gpu_placeholder_btn = QPushButton("Placeholder - GPU cracking panel")
        gpu_layout.addWidget(gpu_placeholder_btn)
        self.gpucrack_widget.setLayout(gpu_layout)
        self.nettools_toolbox.addItem(self.gpucrack_widget, "GPU cracking panel")

        # 5) Container ephemeral environment
        self.container_widget = QWidget()
        container_layout = QVBoxLayout(self.container_widget)
        container_placeholder_btn = QPushButton("Placeholder - Container ephemeral environment")
        container_layout.addWidget(container_placeholder_btn)
        self.container_widget.setLayout(container_layout)
        self.nettools_toolbox.addItem(self.container_widget, "Container ephemeral env")

        # 6) Keylogger demo
        self.keylogger_widget = QWidget()
        keylog_layout = QVBoxLayout(self.keylogger_widget)
        keylog_placeholder_btn = QPushButton("Placeholder - Keylogger demo")
        keylog_layout.addWidget(keylog_placeholder_btn)
        self.keylogger_widget.setLayout(keylog_layout)
        self.nettools_toolbox.addItem(self.keylogger_widget, "Keylogger demo")

        # 7) Hardening manager
        self.hardening_widget = QWidget()
        hardening_layout = QVBoxLayout(self.hardening_widget)
        hard_placeholder_btn = QPushButton("Placeholder - Hardening manager")
        hardening_layout.addWidget(hard_placeholder_btn)
        self.hardening_widget.setLayout(hardening_layout)
        self.nettools_toolbox.addItem(self.hardening_widget, "Hardening manager")

        self.nettools_page.setLayout(self.nettools_layout)
        self.main_toolbox.addItem(self.nettools_page, "[nettools]")

        self.main_layout.addWidget(self.menu_widget, 1)
        self.main_layout.addWidget(self.main_toolbox, 3)

        self.results_data = []

        # Harmonogram - bez zmian
        run_scheduler_in_background()

    # ------------------ METODY KLIKNIĘĆ (placeholder) ------------------
    def on_start_button_clicked(self):
        pass

    def on_history_button_clicked(self):
        pass

    def on_export_button_clicked(self):
        pass

    def on_filter_button_clicked(self):
        pass

    def on_theme_button_clicked(self):
        pass

    def on_schedule_button_clicked(self):
        pass

    def on_clear_button_clicked(self):
        pass

    # ------------------ METODY ZAKŁADKI 3: FuzzScrap ------------------
    def run_simple_fuzz(self):
        url_base = self.fuzz_url_input.text().strip()
        param_name = self.fuzz_param_input.text().strip()
        fuzz_words = [w.strip() for w in self.fuzz_words_input.text().split(",") if w.strip()]

        results = simple_get_fuzz(url_base, param_name, fuzz_words)
        self.update_fuzz_table(results)

    def run_directory_bruteforce(self):
        domain_url = self.dir_url_input.text().strip()
        wordlist = [w.strip() for w in self.dir_wordlist_input.text().split(",") if w.strip()]
        results = directory_bruteforce(domain_url, wordlist)
        self.update_fuzz_table(results)

    def update_fuzz_table(self, fuzz_results):
        self.fuzz_results_table.setRowCount(len(fuzz_results))
        for i, item in enumerate(fuzz_results):
            url_item = QTableWidgetItem(item.get("url", ""))
            self.fuzz_results_table.setItem(i, 0, url_item)

            status_val = ""
            if "status_code" in item:
                status_val = str(item["status_code"])
            elif "error" in item:
                status_val = "ERROR"
            self.fuzz_results_table.setItem(i, 1, QTableWidgetItem(status_val))

            sample_val = item.get("content_sample", "") or item.get("error", "")
            self.fuzz_results_table.setItem(i, 2, QTableWidgetItem(sample_val))

    # ------------------ METODY ZAKŁADKI 4: AI/Analysis ------------------
    def test_sentiment(self):
        link = self.ai_link_input.text().strip()
        result = simple_sentiment_analysis(link)
        self.ai_results_box.appendPlainText(f"[Sentiment] Wynik: {result}")

    def test_link_classify(self):
        link = self.ai_link_input.text().strip()
        result = classify_link(link)
        self.ai_results_box.appendPlainText(f"[LinkClassifier] {link} -> {result}")

    def test_summary(self):
        text = "Bardzo długi tekst... (w realu pobrane z jakiejś strony). Treść, treść, treść..."
        summary = simple_summary(text, max_length=50)
        self.ai_results_box.appendPlainText(f"[Summary] {summary}")

    def test_forum_analyze(self):
        fake_forum_text = "Witajcie, ten mecz był super! Naprawdę super i mega! A spam? Nie, nienawidzę spamu!"
        top_words = analyze_forum_threads(fake_forum_text)
        self.ai_results_box.appendPlainText(f"[Forum] Top słowa: {top_words}")

    def test_recommendations(self):
        history = ["http://example.com/sport", "http://example.com/promo2"]
        candidates = ["http://example.com/promo3", "http://example.com/tech_news"]
        reco = recommend_links(history, candidates)
        self.ai_results_box.appendPlainText(f"[Recommendations] {reco}")

    def test_spam_detect(self):
        text = "Wygrałeś 1000$ w loterii prince nigeria - odpisz!"
        is_spam = detect_spam_phishing(text)
        self.ai_results_box.appendPlainText(f"[SpamDetect] spam={is_spam}")

    def test_topic_modelling(self):
        text = "To był niesamowity mecz piłki nożnej w lidze mistrzów. Sport górą!"
        category = simple_topic_detect(text)
        self.ai_results_box.appendPlainText(f"[TopicModelling] Kategoria: {category}")

    def test_social_sentiment(self):
        hashtag = "#promo2023"
        result = mock_twitter_sentiment(hashtag)
        self.ai_results_box.appendPlainText(f"[SocialSentiment] {hashtag} -> {result}")

    def test_popularity(self):
        link = self.ai_link_input.text().strip()
        pop = check_popularity(link)
        self.ai_results_box.appendPlainText(f"[Popularity] {link} -> {pop} wzmianek")

    def test_fake_ocr(self):
        img_path = "/home/dev/Desktop/example.png"
        ocr_result = fake_ocr(img_path)
        self.ai_results_box.appendPlainText(f"[FakeOCR] {ocr_result}")

    # ------------------ METODY ZAKŁADKI 5: GUI/Data ------------------
    def show_dashboard_example(self):
        links = [r["url"] for r in self.results_data]
        chart_info = get_chart_data(links)
        pie_data = generate_pie_data(chart_info["domain_counts"])
        self.gdata_output.appendPlainText(f"[Dashboard] Domeny:\n{pie_data}")

    def remove_last_column(self):
        col_count = 0
        if col_count > 0:
            remove_custom_column(self, col_count - 1)

    def enable_dragdrop_main_table(self):
        self.gdata_output.appendPlainText("[DragDrop] Włączono drag&drop na results_table.")

    def make_main_table_editable(self):
        self.gdata_output.appendPlainText("[Editable] Tabela główna jest edytowalna.")

    def test_timeline(self):
        link = "http://testlink.com/"
        add_link_to_timeline(self.timeline_data, link)
        out = get_timeline_display(self.timeline_data)
        self.gdata_output.appendPlainText(f"[Timeline]\n{out}")

    def test_config_save_load(self):
        config = load_config()
        set_theme(config, "dark")
        save_config(config)
        new_conf = load_config()
        current_theme = get_theme(new_conf)
        self.gdata_output.appendPlainText(f"[Config] Ustawiono motyw = {current_theme}")

    # ------------------ METODY ZAKŁADKI 6: Net/API ------------------
    def test_db_init(self):
        init_db()
        self.netapi_output.appendPlainText("[DB] Zainicjalizowano bazę SQLite.")

    def test_db_save(self):
        url = "http://example.com"
        save_link_to_db(url)
        self.netapi_output.appendPlainText(f"[DB] Zapisano do bazy: {url}")

    def test_db_load(self):
        rows = load_history_from_db()
        self.netapi_output.appendPlainText("[DB] Historia z bazy:")
        for r in rows:
            self.netapi_output.appendPlainText(str(r))

    def test_email_send(self):
        result = send_email_with_attachment(
            host="smtp.gmail.com",
            port=587,
            login="twoj.login@gmail.com",
            password="twoje.haslo",
            to_addr="cel@example.com",
            subject="Test mail",
            body="Cześć, to jest test.",
            attachment_path=None
        )
        self.netapi_output.appendPlainText(f"[Email] Wysłano={result}")

    def test_chat_send(self):
        slack_res = send_slack_message("https://hooks.slack.com/services/FAKE/WEBHOOK", "Hello Slack!")
        self.netapi_output.appendPlainText(f"[Chat] Slack - {slack_res}")
        tg_res = send_telegram_message("FAKE_BOT_TOKEN", "123456789", "Hello Telegram!")
        self.netapi_output.appendPlainText(f"[Chat] Telegram - {tg_res}")

    def test_plugin_manager(self):
        plugins = load_plugins("plugins")
        self.netapi_output.appendPlainText(f"[PluginManager] Załadowano: {plugins}")

    def test_graphql(self):
        query_str = "{ allLinks { url content } }"
        response = execute_graphql(query_str)
        self.netapi_output.appendPlainText(f"[GraphQL] {response}")

    def test_geocode(self):
        coords = geocode_address("Warsaw")
        self.netapi_output.appendPlainText(f"[Geo] Warsaw -> {coords}")

    def test_dockerfile(self):
        create_dockerfile("Dockerfile")
        self.netapi_output.appendPlainText("[Docker] Utworzono Dockerfile.")

    def test_encrypt(self):
        enc = net_encrypt_data("sekret", "mykey")
        self.netapi_output.appendPlainText(f"[Encrypt NetAPI] -> {enc}")
        dec = net_decrypt_data(enc, "mykey")
        self.netapi_output.appendPlainText(f"[Decrypt NetAPI] -> {dec}")

    # ------------------ METODY ZAKŁADKI 7: Sec/Automation ------------------
    def test_encrypt_decrypt(self):
        encrypted = encrypt_data("hello", "mykey")
        self.secauto_output.appendPlainText(f"[Encrypt] -> {encrypted}")
        decrypted = decrypt_data(encrypted, "mykey")
        self.secauto_output.appendPlainText(f"[Decrypt] -> {decrypted}")

    def test_run_tests(self):
        success = run_basic_tests()
        self.secauto_output.appendPlainText(f"[Tests] Wynik: {success}")

    def test_security_scan(self):
        url = "http://example.com/<script>"
        found = simple_security_scan(url)
        self.secauto_output.appendPlainText(f"[SecurityScan] Znalezione frazy: {found}")

    def test_audit_logs(self):
        matches = filter_logs("debug.log", "ERROR")
        self.secauto_output.appendPlainText("[AuditLog] Linijki z 'ERROR':")
        for line in matches:
            self.secauto_output.appendPlainText(line)

    def test_migrations(self):
        run_migration()
        self.secauto_output.appendPlainText("[Migrations] Zakończono migracje DB.")

    def test_ci_cd(self):
        res = run_ci_pipeline()
        self.secauto_output.appendPlainText(f"[CI/CD] Wynik: {res}")

    def test_profiling(self):
        def dummy_scrape():
            start_scraping(self)
        _, elapsed = profile_function(dummy_scrape)
        self.secauto_output.appendPlainText(f"[Profiling] Czas scrapowania: {elapsed:.2f}s")

    def test_fuzz_plugins(self):
        words = load_fuzz_dictionary("fuzz_dictionary.txt")
        self.secauto_output.appendPlainText(f"[FuzzPlugins] Wczytane słowa: {words}")

    def test_cli_mode(self):
        args = parse_cli_args()
        self.secauto_output.appendPlainText(f"[CLI] headless={args.headless}, url={args.url}")

    def test_duplicates(self):
        link = "http://example.com"
        known_links = {"http://example.com", "http://test.com"}
        is_dup = check_duplicates(link, known_links)
        self.secauto_output.appendPlainText(f"[Duplicates] {link} -> {is_dup}")

    # ------------------ METODY ZAKŁADKI nettools : firewall ------------------
    def run_firewall_demo(self):
        from ui.bookmarks.nettools.firewall_handler import list_iptables_rules
        output = list_iptables_rules()
        QMessageBox.information(self, "Firewall Demo", output)

    def run_block_ip(self, ip):
        from ui.bookmarks.nettools.firewall_handler import add_block_rule
        output = add_block_rule(ip)
        QMessageBox.information(self, "Firewall Demo", output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
