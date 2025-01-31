"""
chat_handler.py
Keyword: net_api_chat

Wysyłanie powiadomień do kanału Slack/Telegram.
Uproszczona wersja Slack (webhook) i Telegram (token+chat_id).
"""

import requests

def send_slack_message(webhook_url, text):
    """
    Wysyła komunikat do Slacka przez webhook_url.
    """
    payload = {"text": text}
    try:
        r = requests.post(webhook_url, json=payload, timeout=5)
        return r.status_code == 200
    except requests.RequestException as e:
        print(f"Slack error: {e}")
        return False

def send_telegram_message(bot_token, chat_id, text):
    """
    Wysyła komunikat do Telegrama używając Bot API.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    try:
        r = requests.get(url, params=params, timeout=5)
        return r.status_code == 200
    except requests.RequestException as e:
        print(f"Telegram error: {e}")
        return False
