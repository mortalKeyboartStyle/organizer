"""
geoapi_handler.py
Keyword: net_api_geo

Z linków z danymi adresowymi wyodrębnianie punktów, wyświetlanie na mapie.
Tu - atrapa: wysyłamy zapytanie do map API z adresem i odbieramy koordynaty.
"""

import requests

def geocode_address(address):
    """
    Używa np. Nominatim (OpenStreetMap) do geokodowania. Atrapa.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json"
    }
    try:
        r = requests.get(url, params=params, timeout=5)
        data = r.json()
        if data:
            return (data[0]["lat"], data[0]["lon"])
        return None
    except requests.RequestException as e:
        print(f"Geocode error: {e}")
        return None
