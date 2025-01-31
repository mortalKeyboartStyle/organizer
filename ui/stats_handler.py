def generate_statistics(data):
	"""Tworzy statystyki z wyników."""
	total_results = len(data)
	unique_urls = len(set(item["url"] for item in data))
	return {
		"total_results": total_results,
		"unique_urls": unique_urls,
	}

# Keyword: stats_handler_basic
