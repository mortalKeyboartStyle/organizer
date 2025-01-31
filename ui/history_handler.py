import os

HISTORY_FILE = "history.txt"

def save_to_history(url):
    """Zapisuje URL do historii wyszukiwań."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(url + "\n")

def load_history():
    """Wczytuje historię wyszukiwań."""
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
    
# Keyword: history_handler_basic
