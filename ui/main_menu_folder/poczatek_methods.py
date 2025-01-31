import logging
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

# Importy z Twoich modułów do fuzzscrap
from ui.bookmarks.fuzzscrap.web_fuzzing_handler import simple_get_fuzz
from ui.bookmarks.fuzzscrap.extended_fuzz_handler import directory_bruteforce

# Importy z AI/Analysis
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

# Importy z GUI/Data (np. kiosk_mode, tabs_handler, columns_config, etc.)
from ui.bookmarks.gui_data.kiosk_mode import enable_kiosk_mode, disable_kiosk_mode
from ui.bookmarks.gui_data.tabs_handler import add_new_tab
from ui.bookmarks.gui_data.columns_config import add_custom_column, remove_custom_column
from ui.bookmarks.gui_data.multi_user_mode import switch_user
from ui.bookmarks.gui_data.dragdrop_handler import enable_drag_drop_for_table
from ui.bookmarks.gui_data.editable_table import make_table_editable
from ui.bookmarks.gui_data.tray_handler import enable_system_tray
from ui.bookmarks.gui_data.timeline_handler import add_link_to_timeline, get_timeline_display
from ui.bookmarks.gui_data.config_manager import load_config, save_config, get_theme, set_theme

# Importy z Net/API
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

# Importy z Sec/Automation
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


class PoczatekMethods:
    """
    Klasa z metodami logiki dla zakładki [poczatek].
    Obejmuje FuzzScrap, AI/Analysis, GUI/Data, Net/API, Sec/Automation,
    czyli wszystko co jest w QTabWidget w pliku poczatek_tab.py.
    """

    # ------------------ FuzzScrap ------------------
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

    # ------------------ AI/Analysis ------------------
    def test_sentiment(self):
        link = self.ai_link_input.text().strip()
        result = simple_sentiment_analysis(link)
        self.ai_results_box.appendPlainText(f"[Sentiment] Wynik: {result}")

    def test_link_classify(self):
        link = self.ai_link_input.text().strip()
        result = classify_link(link)
        self.ai_results_box.appendPlainText(f"[LinkClassifier] {link} -> {result}")

    def test_summary(self):
        text = "Bardzo długi tekst... (placeholder) w realu pobrane z jakiejś strony."
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

    # ------------------ GUI/Data ------------------
    def show_dashboard_example(self):
        # Przykład: budowanie chart_info i wyświetlanie w self.gdata_output
        # W realu: from ui.bookmarks.gui_data.dashboard_handler import get_chart_data, ...
        links = [r["url"] for r in self.results_data]
        chart_info = {"domain_counts": {"example.com": 5, "test.com": 2}}
        # Ewentualnie: chart_info = get_chart_data(links)
        # ...
        self.gdata_output.appendPlainText(f"[Dashboard] Domeny:\n{chart_info}")

    def remove_last_column(self):
        # Placeholder. W realu: remove_custom_column(self, idx)
        pass

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

    # ------------------ Net/API ------------------
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

    # ------------------ Sec/Automation ------------------
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
            start_scraping(self)  # lub cokolwiek
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
