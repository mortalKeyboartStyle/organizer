import logging
from PyQt6.QtWidgets import QMessageBox
from src.scraper import fetch_page
from src.parser import parse_html
from src.database import save_result
from src.file_manager import get_or_create_directory, save_to_csv

def start_scraping(main_window, url=None):
	"""
	Funkcja obsługująca proces scrapowania.
	:param main_window: Instancja głównego okna aplikacji (do aktualizacji GUI).
	:param url: URL do przetworzenia (opcjonalnie).
	"""
	logging.debug("Rozpoczęcie przetwarzania URL...")

	# Pobranie URL z pola tekstowego, jeśli nie podano jako argumentu
	if url is None:
		raw_url = main_window.url_input.text().strip()
		logging.debug(f"Wartość z pola tekstowego (przed przygotowaniem): {raw_url}")
		url = main_window.prepare_url(raw_url)
		logging.debug(f"Wartość URL po przygotowaniu: {url}")

	# Sprawdzanie, czy URL jest pusty
	if not raw_url:
		QMessageBox.warning(main_window, "Błąd", "Proszę podać adres URL.")
		logging.error("Podano pusty URL.")
		return

	# Sprawdzanie poprawności URL
	if not main_window.is_valid_url(url):
		QMessageBox.warning(main_window, "Błąd", "Podano niepoprawny adres URL.")
		logging.error(f"Niepoprawny URL: {url}")
		return

	try:
		# Pobranie zawartości strony
		html = fetch_page(url)
		logging.debug(f"Pobrano zawartość strony dla URL: {url}")
		if html and not html.startswith("Błąd"):
			tag = "a"
			main_window.results_data = [
				{"url": url, "content": result.get("href")}
				for result in parse_html(html, tag) if result.get("href")
			]

			# Zapis wyników
			directory = get_or_create_directory(url)
			save_to_csv(directory, main_window.results_data)
			for result in main_window.results_data:
				save_result(url, result["content"])

			# Aktualizacja GUI
			main_window.update_table(main_window.results_data)
			main_window.update_statistics()
			QMessageBox.information(main_window, "Sukces", f"Dane zapisane w {directory}")
		else:
			QMessageBox.critical(main_window, "Błąd", "Nie udało się pobrać strony.")
			logging.error(f"Nie udało się pobrać zawartości dla URL: {url}")
	except Exception as e:
		QMessageBox.critical(main_window, "Błąd", f"Wystąpił błąd: {e}")
		logging.exception(f"Błąd podczas przetwarzania URL: {url}")
