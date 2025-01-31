# filter_handler.py
# Keyword: filter_handler_basic

def filter_results(results, include_keywords=None, exclude_keywords=None):
    """
    Filtrowanie wyników według słów kluczowych.
    :param results: lista słowników {"url": ..., "content": ...}
    :param include_keywords: lista słów, które wynik MUSI zawierać
    :param exclude_keywords: lista słów, które powodują odrzucenie wyniku
    :return: przefiltrowana lista wyników
    """
    if include_keywords is None:
        include_keywords = []
    if exclude_keywords is None:
        exclude_keywords = []

    filtered = []
    for item in results:
        text = f"{item['url']} {item['content']}".lower()

        # Sprawdzanie słów kluczowych, które muszą się pojawić
        if any(kw.lower() not in text for kw in include_keywords):
            continue

        # Sprawdzanie słów kluczowych, które wykluczają wynik
        if any(kw.lower() in text for kw in exclude_keywords):
            continue

        filtered.append(item)
    return filtered
