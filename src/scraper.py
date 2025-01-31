import requests

def fetch_page(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; WyszukiwaczPromocji/1.0)"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Błąd pobierania {url}: {e}"
