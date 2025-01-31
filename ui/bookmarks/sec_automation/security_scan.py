"""
security_scan.py
Keyword: sec_automation_security_scan

Podstawowy skaner luk (np. XSS, SQL injection).
Tu - szukanie słów kluczowych w URL/parametrach.
"""

def simple_security_scan(url):
	"""
	Sprawdza, czy w url występują podejrzane frazy typu <script> lub ' UNION '.
	"""
	sus_keywords = ["<script>", " union ", "' or '1'='1", "select * from"]
	url_lower = url.lower()
	found = [kw for kw in sus_keywords if kw in url_lower]
	return found  # lista znalezionych podejrzanych
