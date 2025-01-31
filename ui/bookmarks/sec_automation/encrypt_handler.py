"""
encrypt_handler.py
Keyword: sec_automation_encrypt

Szyfrowanie wrażliwych danych (np. haseł, tokenów API).
Prosty przykład z 'cryptography' lub tutaj - uproszczona atrapa base64.
"""

import base64

def encrypt_data(data, key="secret"):
	"""
	Uproszczona atrapa: base64 + key. W realu: AES/GCM (cryptography).
	"""
	combined = (key + data).encode("utf-8")
	return base64.b64encode(combined).decode("utf-8")

def decrypt_data(token, key="secret"):
	decoded = base64.b64decode(token).decode("utf-8")
	if decoded.startswith(key):
		return decoded[len(key):]
	return None
