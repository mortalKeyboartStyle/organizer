"""
multi_thread_scraping.py
Keyword: fuzzscrap_multithreading

Prosty moduł wielowątkowy do pobierania wielu URL-i równolegle.
"""

import requests
from concurrent.futures import ThreadPoolExecutor

def multi_thread_fetch(urls, max_workers=5):
    """
    Pobiera treść z listy URL-i przy pomocy wielowątkowości.
    Zwraca listę słowników: {"url":..., "status_code":..., "content":...}.
    """
    results = []

    def fetch(url):
        try:
            r = requests.get(url, timeout=5)
            return {"url": url, "status_code": r.status_code, "content": r.text}
        except requests.RequestException as e:
            return {"url": url, "error": str(e)}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(fetch, u): u for u in urls}
        for future in future_to_url:
            data = future.result()
            results.append(data)
    return results
