"""
web_fuzzing_handler.py
Keyword: fuzzscrap_web_fuzzing

Prosty moduł do fuzzingu parametrów URL (GET).
Przykład: fuzzowanie parametru "search" przy użyciu listy słów kluczowych.
"""

import requests

def simple_get_fuzz(url_base, param_name, fuzz_words):
    """
    Dla każdej frazy w fuzz_words tworzy zapytanie GET do:
    url_base?param_name=fraza
    Zwraca listę odpowiedzi (kod statusu, ewentualnie fragment treści).
    """
    results = []
    for word in fuzz_words:
        full_url = f"{url_base}?{param_name}={word}"
        try:
            r = requests.get(full_url, timeout=5)
            result_entry = {
                "url": full_url,
                "status_code": r.status_code,
                "content_sample": r.text[:100]  # pobieramy mały fragment
            }
            results.append(result_entry)
        except requests.RequestException as e:
            results.append({
                "url": full_url,
                "error": str(e)
            })
    return results
