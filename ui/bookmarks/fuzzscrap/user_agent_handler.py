"""
user_agent_handler.py
Keyword: fuzzscrap_user_agent

Zmiana nagłówków, by scrapować w sposób zbliżony do popularnych przeglądarek.
"""

import requests

def fetch_with_agent(url, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/96.0"):
    """
    Wysyła zapytanie GET z podanym User-Agent.
    """
    headers = {"User-Agent": user_agent}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        return r.text
    except requests.RequestException as e:
        print(f"Błąd: {e}")
        return None
