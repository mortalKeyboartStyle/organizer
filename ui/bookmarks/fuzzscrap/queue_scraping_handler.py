"""
queue_scraping_handler.py
Keyword: fuzzscrap_queue

Zadania scrapingu trafiają do kolejki i są przetwarzane asynchronicznie.
Przykład w wersji uproszczonej (list zamiast RabbitMQ).
"""

import time
import threading

class SimpleScrapingQueue:
    def __init__(self):
        self.queue = []
        self.is_running = False

    def add_task(self, url):
        self.queue.append(url)

    def process_tasks(self, fetch_function):
        """
        Uruchamia przetwarzanie zadań w osobnym wątku.
        fetch_function – funkcja do pobierania (np. requests.get).
        """
        if self.is_running:
            return
        self.is_running = True

        def worker():
            while self.queue:
                url = self.queue.pop(0)
                print(f"Scraping: {url}")
                time.sleep(1)  # symulacja
                fetch_function(url)
            self.is_running = False

        threading.Thread(target=worker, daemon=True).start()
