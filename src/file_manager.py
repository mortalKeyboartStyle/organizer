import os
import re
import csv

BASE_DIR = "data"

def generate_directory_name(url):
    clean_url = re.sub(r"https?://(www\.)?", "", url)
    return re.sub(r"[^\w]", "", clean_url)

def get_or_create_directory(url):
    dir_name = generate_directory_name(url)
    full_path = os.path.join(BASE_DIR, dir_name)
    os.makedirs(full_path, exist_ok=True)
    return full_path

def save_to_csv(directory, data):
    file_path = os.path.join(directory, "results.csv")
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["URL", "Zawartość"])
        for row in data:
            writer.writerow([row["url"], row["content"]])
