"""
extended_fuzz_handler.py
Keyword: fuzzscrap_extended_fuzz

Bruteforce ścieżek, np. /admin, /login, /secret – poszukiwanie ukrytych folderów.
"""

import requests

def directory_bruteforce(domain_url, wordlist):
    """
    Dołącza każdą frazę z wordlist do domain_url (bez / na końcu).
    Sprawdza status_code.
    """
    results = []
    if domain_url.endswith("/"):
        domain_url = domain_url[:-1]

    for word in wordlist:
        test_path = f"{domain_url}/{word}"
        try:
            r = requests.get(test_path, timeout=5)
            results.append({"url": test_path, "status_code": r.status_code})
        except requests.RequestException as e:
            results.append({"url": test_path, "error": str(e)})

    return results
