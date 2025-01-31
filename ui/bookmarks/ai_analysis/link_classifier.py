"""
link_classifier.py
Keyword: ai_analysis_link_classifier

Prosty model ML oceniający, czy link jest "atrakcyjny" (promocyjny) czy nie.
Na razie - reguły oparte na słowach kluczowych.
"""

def classify_link(url):
    """
    Zwraca 'promocyjny' lub 'zwykły' w zależności od zawartości URL.
    """
    promo_keywords = ["promo", "discount", "sale", "lastminute", "okazja"]
    url_lower = url.lower()
    if any(kw in url_lower for kw in promo_keywords):
        return "promocyjny"
    return "zwykły"
