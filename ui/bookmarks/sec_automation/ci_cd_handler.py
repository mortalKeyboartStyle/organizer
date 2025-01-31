"""
ci_cd_handler.py
Keyword: sec_automation_ci_cd

Skrypt wspomagający pipeline (GitLab CI, GitHub Actions) - automatyczna budowa, test.
W praktyce to np. plik .yml; tu - atrapa w Pythonie do uruchamiania testów.
"""

import subprocess

def run_ci_pipeline():
	"""
	Uruchamia np. 'pytest' i 'flake8'.
	"""
	try:
		print("[CI] Uruchamiam pytest...")
		subprocess.check_call(["pytest", "--maxfail=1"])
		print("[CI] Uruchamiam flake8...")
		subprocess.check_call(["flake8", "."])
		print("[CI] Pipeline zakończony sukcesem.")
		return True
	except subprocess.CalledProcessError as e:
		print(f"[CI] Błąd w pipeline: {e}")
		return False
