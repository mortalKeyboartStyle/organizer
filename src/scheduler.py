import schedule
import time

def job():
    print("Wykonuję zaplanowane zadanie...")

def start_scheduler():
    schedule.every(1).hour.do(job)
    print("Harmonogram uruchomiony. Oczekiwanie na zaplanowane zadania...")
    while True:
        schedule.run_pending()
        time.sleep(1)
