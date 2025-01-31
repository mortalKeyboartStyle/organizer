"""
encrypt_handler.py
Keyword: net_api_encrypt

Szyfrowanie wrażliwych danych (np. tokenów, haseł) za pomocą cryptography (AES, itp.).
Tu - atrapa z base64.
"""

import base64

def encrypt_data(data, key="secret"):
    """
    Prosta atrapa, base64 + key. W realu: AES/GCM itp.
    """
    combined = (key + data).encode("utf-8")
    return base64.b64encode(combined).decode("utf-8")

def decrypt_data(token, key="secret"):
    decoded = base64.b64decode(token)
    decoded_str = decoded.decode("utf-8")
    # usuwamy prefix "key"
    if decoded_str.startswith(key):
        return decoded_str[len(key):]
    return None
