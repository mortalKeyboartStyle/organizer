"""
audit_log_handler.py
Keyword: sec_automation_audit_log

Zaawansowane przeglądanie i filtrowanie logów, raporty incydentów.
Tu - przykład prostego filtra słowa "ERROR".
"""

import os

def filter_logs(log_path, keyword="ERROR"):
	"""
	Zwraca listę linii z pliku log_path zawierających 'keyword'.
	"""
	if not os.path.exists(log_path):
		return []
	matching = []
	with open(log_path, "r", encoding="utf-8") as f:
		for line in f:
			if keyword in line:
				matching.append(line.strip())
	return matching
