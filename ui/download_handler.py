# proxy_handler.py
# Keyword: proxy_handler_basic

import requests

def fetch_page_with_proxy(url, proxy_url=None):
	"""
	Pobiera stronę przez podany proxy_url (np. http://123.123.123.123:8080).
	Jeśli proxy_url=None, łączy się bezpośrednio.
	"""
	try:
		if proxy_url:
			proxies = {
				"http": proxy_url,
				"https": proxy_url,
			}
			response = requests.get(url, proxies=proxies, timeout=10)
		else:
			response = requests.get(url, timeout=10)
		response.raise_for_status()
		return response.text
	except requests.RequestException as e:
		print(f"Błąd pobierania z proxy: {proxy_url}, {e}")
		return None
