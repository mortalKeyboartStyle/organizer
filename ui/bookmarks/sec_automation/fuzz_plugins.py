"""
fuzz_plugins.py
Keyword: sec_automation_fuzz_plugins

Możliwość doładowywania własnych wzorców fuzzingu, dictionary. 
Tu - atrapa wczytująca plik .txt z 'dictionary' i zwraca listę słów.
"""

import os

def load_fuzz_dictionary(dict_path="fuzz_dictionary.txt"):
	"""
	Wczytuje słowa z pliku, zwraca jako listę.
	"""
	if not os.path.exists(dict_path):
		return []
	with open(dict_path, "r", encoding="utf-8") as f:
		return [line.strip() for line in f if line.strip()]
