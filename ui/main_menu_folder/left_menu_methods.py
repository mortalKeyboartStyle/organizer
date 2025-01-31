class LeftMenuMethods:
    """
    Klasa z metodami obsługującymi przyciski w lewym menu.
    Dziedziczy ją klasa MainWindow (w main_window.py).
    Dzięki temu w pliku left_menu.py możemy pisać:
       start_button.clicked.connect(main_window.on_start_button_clicked)
    a tu faktyczna implementacja.
    """

    def on_start_button_clicked(self):
        """ Obsługa kliknięcia przycisku 'Start' (np. uruchom scraping). """
        # Przykład:
        # url = self.url_input.text().strip()
        # ... logika ...
        print("[LeftMenu] on_start_button_clicked - placeholder")

    def on_history_button_clicked(self):
        """ Obsługa kliknięcia przycisku 'Pokaż historię'. """
        # Przykład:
        # history = load_history()
        # QMessageBox.information(self, "Historia", "\n".join(history))
        print("[LeftMenu] on_history_button_clicked - placeholder")

    def on_export_button_clicked(self):
        """ Obsługa kliknięcia przycisku 'Eksportuj wyniki'. """
        # Przykład:
        # if self.results_data:
        #     save_to_csv("export.csv", self.results_data)
        #     QMessageBox.information(self, "Eksport", "Wyniki zapisane do export.csv")
        print("[LeftMenu] on_export_button_clicked - placeholder")

    def on_filter_button_clicked(self):
        """ Obsługa kliknięcia przycisku 'Filtry (przykładowe)'. """
        # Przykład:
        # show_filters_dialog()
        print("[LeftMenu] on_filter_button_clicked - placeholder")

    def on_theme_button_clicked(self):
        """ Obsługa kliknięcia przycisku 'Zmień motyw'. """
        # Przykład:
        # apply_theme("dark") lub togglowanie
        print("[LeftMenu] on_theme_button_clicked - placeholder")

    def on_schedule_button_clicked(self):
        """ Obsługa kliknięcia przycisku 'Zaplanuj zadanie (test)'. """
        # Przykład:
        # schedule_job("my_task", interval=3600)
        print("[LeftMenu] on_schedule_button_clicked - placeholder")

    def on_clear_button_clicked(self):
        """ Obsługa kliknięcia przycisku 'Wyczyść wyniki'. """
        # Przykład:
        # self.results_data = []
        # self.update_results_table()
        print("[LeftMenu] on_clear_button_clicked - placeholder")
