"""
forum_handler.py
Keyword: ai_analysis_forum

Przeszukiwanie forów / komentarzy i wykrywanie popularnych tematów.
Na razie - prosta analiza częstych słów.
"""

from collections import Counter
import re

def analyze_forum_threads(text):
    """
    Wyszukuje najczęściej występujące słowa (poza stoplistą).
    Zwraca listę (słowo, liczba wystąpień).
    """
    stop_words = {"the", "and", "or", "i", "you", "jest", "oraz"}
    words = re.findall(r"[a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", text.lower())
    filtered = [w for w in words if w not in stop_words]
    counter = Counter(filtered)
    return counter.most_common(10)
