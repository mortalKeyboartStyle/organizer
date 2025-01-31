"""
duplicate_detector.py
Keyword: sec_automation_duplicates

Odczytywanie linków i sprawdzanie w bazie, czy link już istnieje.
Na razie - atrapa bazująca na zewnętrznej liście/storze.
"""

def check_duplicates(link, known_links):
	"""
	Zwraca True, jeśli link już jest w known_links.
	"""
	return link in known_links
