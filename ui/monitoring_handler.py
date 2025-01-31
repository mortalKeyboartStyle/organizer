# monitoring_handler.py
# Keyword: monitoring_handler_basic

import hashlib

def get_page_signature(html_content):
	"""
	Zwraca skrót (hash) treści HTML, by szybko porównać zmiany.
	"""
	return hashlib.md5(html_content.encode("utf-8")).hexdigest()

def compare_signatures(old_sig, new_sig):
	"""
	Sprawdza, czy sygnatura uległa zmianie.
	"""
	return old_sig != new_sig

def monitor_page(main_window, url, stored_signatures):
	"""
	Monitoruje daną stronę (url), porównując bieżącą sygnaturę z zapisaną.
	stored_signatures to słownik { url: signature }.
	"""
	html = main_window.fetch_html_directly(url)  
	# fetch_html_directly to przykładowa metoda/funkcja, która zwróci zawartość strony
	# (możesz użyć scraping_handler lub innej implementacji)

	if not html:
		return f"Brak danych dla {url}"

	new_sig = get_page_signature(html)
	old_sig = stored_signatures.get(url)

	if old_sig:
		if compare_signatures(old_sig, new_sig):
			stored_signatures[url] = new_sig
			return f"Znaleziono zmiany w {url}!"
		else:
			return f"Brak zmian w {url}."
	else:
		# Pierwsze zapisanie sygnatury
		stored_signatures[url] = new_sig
		return f"Pierwsze monitorowanie {url}. Sygnatura zapisana."
