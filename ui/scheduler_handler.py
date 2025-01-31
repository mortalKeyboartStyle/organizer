# scheduler_handler.py
# Keyword: scheduler_handler_basic

import schedule
import time
import threading

def schedule_job(main_window, url_list):
    """
    Tworzy zaplanowane zadania na podstawie listy URL-i.
    Można tu dodać parametr z częstotliwością.
    """
    def job():
        for url in url_list:
            main_window.start_scraping(url)  # lub scraping_handler.start_scraping
        print("Wykonano zaplanowane zadanie.")

    schedule.every(1).day.at("12:00").do(job)

def run_scheduler_in_background():
    """
    Uruchamia harmonogram w osobnym wątku.
    """
    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    threading.Thread(target=run_schedule, daemon=True).start()
