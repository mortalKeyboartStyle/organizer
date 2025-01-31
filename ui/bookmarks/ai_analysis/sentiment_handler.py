"""
sentiment_handler.py
Keyword: ai_analysis_sentiment

Rozpoznawanie tonów tekstu (pozytywny/negatywny).
Tu pokazano uproszczony przykład z "słownikiem" sentymentów.
"""

def simple_sentiment_analysis(text):
    """
    Prosty przykład: zlicza słowa pozytywne/negatywne i zwraca 'positive', 'negative' lub 'neutral'.
    """
    positive_words = ["good", "great", "awesome", "promocja", "super"]
    negative_words = ["bad", "terrible", "spam", "ugly", "błąd"]

    text_lower = text.lower()
    pos_count = sum(1 for w in positive_words if w in text_lower)
    neg_count = sum(1 for w in negative_words if w in text_lower)

    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    else:
        return "neutral"
