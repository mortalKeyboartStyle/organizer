"""
topic_modelling.py
Keyword: ai_analysis_topic_modelling

Grupowanie stron w kategorie tematyczne (sport, news, tech, itp.)
Prosty przykład: stwierdzenie 'kategorii' na podstawie słów kluczowych.
"""

def simple_topic_detect(text):
    categories = {
        "sport": ["football", "sport", "mecz", "liga"],
        "news": ["breaking", "update", "news", "report"],
        "tech": ["tech", "it", "software", "hardware"],
    }

    text_lower = text.lower()
    max_hits = 0
    final_cat = "inne"

    for cat, words in categories.items():
        hits = sum(1 for w in words if w in text_lower)
        if hits > max_hits:
            max_hits = hits
            final_cat = cat
    return final_cat
