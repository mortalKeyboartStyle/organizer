import csv

def export_to_csv(file_path, data):
	"""Eksportuje wyniki do pliku CSV."""
	with open(file_path, "w", encoding="utf-8", newline="") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["URL", "Zawartość"])
		for row in data:
			writer.writerow([row["url"], row["content"]])

# Keyword: export_handler_basic
