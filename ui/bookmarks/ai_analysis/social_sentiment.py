"""
social_sentiment.py
Keyword: ai_analysis_social

Integracja z Twitter API (lub innym), liczenie nastroju wokół hasła.
Tu - atrapa bez prawdziwego API.
"""

def mock_twitter_sentiment(hashtag):
    """
    Zwraca udawany 'pozytywny/negatywny' wskaźnik w %.
    """
    # W realnym użyciu: pobieranie tweetów przez Tweepy/requests, analiza sentiment.
    if "promo" in hashtag.lower():
        return {"positive": 70, "negative": 30}
    else:
        return {"positive": 50, "negative": 50}
