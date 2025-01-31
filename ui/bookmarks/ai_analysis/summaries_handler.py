"""
summaries_handler.py
Keyword: ai_analysis_summaries

Generowanie krótkich streszczeń zawartości stron.
Tu - fikcyjna funkcja skracająca tekst do X znaków.
"""

def simple_summary(text, max_length=200):
    """
    Uproszczone "streszczenie", obcina tekst do max_length znaków.
    W realnym przypadku użyj np. modeli GPT/OpenAI, transformers, itp.
    """
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length] + "..."
