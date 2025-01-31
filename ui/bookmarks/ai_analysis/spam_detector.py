"""
spam_detector.py
Keyword: ai_analysis_spam_detector

Analiza linków / treści pod kątem spamu, phishingu.
Proste reguły oparte na słowach kluczowych.
"""

def detect_spam_phishing(text):
    """
    Zwraca True, jeśli wykryto 'spam' / 'phishing', inaczej False.
    """
    spam_words = ["prince nigeria", "paypal verify", "bonus", "wygrana"]
    text_lower = text.lower()
    return any(sw in text_lower for sw in spam_words)
