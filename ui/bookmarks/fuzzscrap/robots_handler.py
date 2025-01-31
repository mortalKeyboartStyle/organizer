"""
robots_handler.py
Keyword: fuzzscrap_robots_txt

Automatyczne pobieranie i analiza robots.txt.
Może blokować scrapowanie ścieżek wymienionych w Disallow.
"""

import requests

def fetch_robots_txt(domain_url):
    """
    Pobiera i zwraca treść pliku robots.txt z danego domain_url
    (np. http://www.example.com).
    """
    if not domain_url.endswith("/"):
        domain_url += "/"
    robots_url = domain_url + "robots.txt"
    try:
        r = requests.get(robots_url, timeout=5)
        r.raise_for_status()
        return r.text
    except requests.RequestException:
        return None

def parse_robots_txt(robots_content):
    """
    Zwraca listę ścieżek "Disallow" - w formie listy stringów.
    """
    disallowed = []
    if not robots_content:
        return disallowed

    for line in robots_content.splitlines():
        line = line.strip()
        if line.lower().startswith("disallow:"):
            path = line.split(":", 1)[1].strip()
            if path:
                disallowed.append(path)
    return disallowed

def is_allowed_path(path, disallow_list):
    """
    Sprawdza, czy dany path nie jest w disallow_list.
    Jeśli jest w disallow_list, zwracamy False.
    """
    for dis in disallow_list:
        if path.startswith(dis):
            return False
    return True
