"""
cli_mode.py
Keyword: sec_automation_cli_mode

Uruchamianie aplikacji z linii poleceń, np.:
python -m wyszukiwacz --headless --url sport.onet.pl
Prosty parser argumentów (argparse).
"""

import argparse

def parse_cli_args():
	parser = argparse.ArgumentParser(description="WyszukiwaczPromocji CLI")
	parser.add_argument("--headless", action="store_true", help="Uruchom w trybie headless")
	parser.add_argument("--url", type=str, help="URL do scrapowania")
	return parser.parse_args()
