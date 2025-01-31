"""
link_registration_handler.py
Keyword: fuzzscrap_link_registration

Dodanie reguł, kiedy linki mają być uważane za ważne,
np. linki wewnętrzne, linki w tej samej domenie.
"""

from urllib.parse import urlparse

def is_internal_link(url, base_domain):
    """
    Sprawdza, czy link prowadzi do tej samej domeny (wewnętrzny).
    """
    parsed_link = urlparse(url)
    return base_domain in parsed_link.netloc

def register_link(url, base_domain, link_storage, only_internal=True):
    """
    Rejestruje link w link_storage (np. liście lub zbiorze),
    z uwzględnieniem, czy linki mają być wewnętrzne.
    """
    if only_internal and not is_internal_link(url, base_domain):
        return False
    if url not in link_storage:
        link_storage.add(url)
        return True
    return False
