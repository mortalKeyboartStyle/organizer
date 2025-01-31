"""
recommendation_handler.py
Keyword: ai_analysis_recommendations

Na podstawie historii i klikalności linków sugerowanie kolejnych stron.
Prosta wersja: jeżeli link zawiera słowa kluczowe, to 'polecany'.
"""

def recommend_links(history, link_candidates):
    """
    :param history: lista odwiedzonych linków
    :param link_candidates: lista linków do oceny
    :return: podlista linków 'polecanych'
    """
    # Prosty przykład: jeśli w historii jest 'sport', to linki z 'sport' w link_candidates będą polecane
    keywords = set()
    for h in history:
        if "sport" in h.lower():
            keywords.add("sport")
        if "promo" in h.lower():
            keywords.add("promo")

    recommended = []
    for candidate in link_candidates:
        lower_candidate = candidate.lower()
        if any(kw in lower_candidate for kw in keywords):
            recommended.append(candidate)

    return recommended
